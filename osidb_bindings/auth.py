"""
osidb-bindings token management
"""

import aiohttp
import requests
from requests_gssapi import HTTPSPNEGOAuth

from .bindings.python_client import AuthenticatedClient, models
from .bindings.python_client.api.auth import (
    auth_token_create,
    auth_token_refresh_create,
    auth_token_retrieve,
)
from .token_cache import TokenCache, resolve_kerberos_principal

# treat tokens as expired this many seconds early
TOKEN_EXPIRY_LEEWAY: int = 30


def is_unauthorized(error: Exception) -> bool:
    """Check whether the sync or async request error is a 401 response"""

    if isinstance(error, requests.HTTPError):
        return error.response is not None and error.response.status_code == 401
    if isinstance(error, aiohttp.ClientResponseError):
        return error.status == 401
    return False


class TokenManager:
    """Provides a valid access token, reusing tokens from memory and the token cache"""

    def __init__(
        self,
        client: AuthenticatedClient,
        auth: tuple[str, str] | str | None,
        refresh_token: str | None = None,
        token_cache_enabled: bool = True,
    ):
        self.client = client
        self.auth = auth
        self.refresh_token: str | None = None
        self.access_token: str | None = None

        if token_cache_enabled:
            if isinstance(auth, tuple):
                identity = auth[0]
            elif auth == "kerberos":
                identity = resolve_kerberos_principal()
            else:
                identity = None
            self.cache: TokenCache | None = TokenCache(
                server_url=client.base_url, identity=identity
            )
        else:
            self.cache = None

        if refresh_token is not None:
            self.store("refresh_token", refresh_token)

    def get_access_token(self, force_refresh: bool = False) -> str:
        """
        Get a valid access token, requesting new tokens only when needed

        Pass force_refresh=True to skip reusing the current access token
        """

        # 1. reuse the access token
        if not force_refresh:
            token = self.lookup("access_token")
            if token is not None:
                return token

        # 2. exchange the refresh token for a new access token
        refresh_token = self.lookup("refresh_token")
        if refresh_token is not None:
            try:
                return self.store(
                    "access_token", self.refresh_access_token(refresh_token)
                )
            except requests.HTTPError as e:
                if not is_unauthorized(e):
                    raise

        # 3. no usable refresh token, log in for both
        return self.login()

    def lookup(self, key: str) -> str | None:
        """Get an unexpired token from memory, then from the token cache"""

        token = getattr(self, key)
        if token is not None and not TokenCache.is_token_expired(
            token, TOKEN_EXPIRY_LEEWAY
        ):
            return token
        token = self.cache.read_token(key, TOKEN_EXPIRY_LEEWAY) if self.cache else None
        if token is not None:
            setattr(self, key, token)
        return token

    def store(self, key: str, token: str) -> str:
        """Store the token in memory and in the token cache"""

        setattr(self, key, token)
        if self.cache:
            self.cache.write_token(key, token)
        return token

    def refresh_access_token(self, refresh_token: str) -> str:
        """Request a new access token from the server using the refresh token"""

        response = auth_token_refresh_create.sync(
            client=self.client,
            body=models.TokenRefreshRequest.from_dict({"refresh": refresh_token}),
        )
        return response.access

    def login(self) -> str:
        """Obtain and store new refresh and access tokens, return the access token"""

        if isinstance(self.auth, tuple):
            response = auth_token_create.sync(
                client=self.client,
                body=models.TokenObtainPairRequest.from_dict(
                    {"username": self.auth[0], "password": self.auth[1]}
                ),
            )
        else:
            response = auth_token_retrieve.sync(
                client=self.client.with_auth(HTTPSPNEGOAuth())
            )
        self.store("refresh_token", response.refresh)
        # access token is optional in the kerberos auth response
        return self.store(
            "access_token",
            response.access or self.refresh_access_token(response.refresh),
        )
