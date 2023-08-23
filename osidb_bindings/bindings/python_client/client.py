import ssl
from typing import Dict, Tuple, Type, Union

import aiohttp
import attr
import requests


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API"""

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(300.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    auth: Union[None, Tuple[str, str], Type[requests.auth.AuthBase]] = attr.ib(
        None, kw_only=True
    )
    async_session: Union[None, aiohttp.ClientSession] = attr.ib(None, kw_only=True)

    def get_auth(self) -> Union[None, Tuple[str, str], Type[requests.auth.AuthBase]]:
        return self.auth

    def with_auth(
        self, auth: Union[None, Tuple[str, str], Type[requests.auth.AuthBase]]
    ) -> "Client":
        """Get a new client matching this one with a new auth method"""
        return attr.evolve(self, auth=auth)

    def get_async_session(self) -> Union[None, aiohttp.ClientSession]:
        return self.async_session

    def with_async_session(
        self, async_session: Union[None, aiohttp.ClientSession]
    ) -> "Client":
        """Get a new client matching this one with a new async session"""
        return attr.evolve(self, async_session=async_session)
