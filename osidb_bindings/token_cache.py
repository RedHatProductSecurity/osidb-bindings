"""
osidb-bindings refresh token file cache
"""

import base64
import datetime
import hashlib
import json
import os
import tempfile
import time
from functools import cached_property
from pathlib import Path

from .helpers import get_env

CACHE_SUBDIR: str = "osidb-bindings"
CACHE_VERSION: int = 1
# owner read/write/execute, no access for group or others
CACHE_DIR_PERMISSIONS: int = 0o700
# owner read/write only, no access for group or others
CACHE_FILE_PERMISSIONS: int = 0o600


def resolve_kerberos_principal() -> str | None:
    """Read the default Kerberos principal from the local credential cache."""
    try:
        import gssapi

        cred = gssapi.Credentials(usage="initiate")
        return str(cred.name)
    except Exception as e:
        print(
            f"WARNING: Failed to resolve Kerberos principal: {e}. "
            "Token cache will not be scoped to identity."
        )
        return None


class TokenCache:
    """Manages reading/writing refresh tokens to disk cache files."""

    def __init__(self, server_url: str, identity: str | None = None) -> None:
        self.server_url: str = server_url
        self.identity: str | None = identity

    @cached_property
    def cache_dir(self) -> Path | None:
        """Resolve the cache directory, trying several locations in order."""
        candidates: list[Path] = []

        env_dir: str | None = get_env("OSIDB_BINDINGS_CACHE_DIR")
        if env_dir:
            candidates.append(Path(env_dir))

        xdg_cache: str | None = get_env("XDG_CACHE_HOME")
        if xdg_cache:
            candidates.append(Path(xdg_cache) / CACHE_SUBDIR)

        try:
            candidates.append(Path.home() / ".cache" / CACHE_SUBDIR)
        except (RuntimeError, OSError):
            pass

        candidates.append(
            Path(tempfile.gettempdir()) / f"{CACHE_SUBDIR}-cache-{os.getuid()}"
        )

        for candidate in candidates:
            try:
                candidate.mkdir(parents=True, exist_ok=True, mode=CACHE_DIR_PERMISSIONS)
                st = candidate.stat()
                if st.st_uid != os.getuid():
                    continue
                return candidate
            except OSError:
                continue

        return None

    @cached_property
    def cache_key(self) -> str:
        """Generate a filesystem-safe cache key from the server URL."""
        normalized: str = self.server_url.lower().rstrip("/")
        if self.identity:
            normalized += f"|{self.identity}"
        return hashlib.sha256(normalized.encode()).hexdigest()[:16]

    def cache_file(self) -> Path | None:
        if self.cache_dir is None:
            return None
        return self.cache_dir / f"{self.cache_key}.json"

    @staticmethod
    def is_token_expired(token: str) -> bool:
        """Check if a JWT token has expired by decoding its payload."""
        try:
            payload: str = token.split(".")[1]
            payload += "=" * (4 - len(payload) % 4)
            claims: dict = json.loads(base64.urlsafe_b64decode(payload))
            return claims["exp"] < time.time()
        except Exception:
            return True

    def read(self) -> str | None:
        """Read cached refresh token, or None if absent/invalid/expired/unreadable."""
        path: Path | None = self.cache_file()
        if path is None or not path.exists():
            return None
        try:
            data = json.loads(path.read_text())
            if not isinstance(data, dict):
                return None
            if data.get("version") != CACHE_VERSION:
                return None
            token: str | None = data.get("refresh_token")
            if token is None or self.is_token_expired(token):
                return None
            return token
        except Exception as e:
            print(
                f"WARNING: Token cache read failed: {e}. "
                "To disable caching, pass token_cache_enabled=False to new_session()."
            )
            return None

    def write(self, token: str) -> None:
        """Write refresh token to cache file with restrictive permissions."""
        path: Path | None = self.cache_file()
        if path is None:
            return
        tmp_path: Path = path.with_suffix(f".tmp.{os.getpid()}")
        try:
            data: str = json.dumps(
                {
                    "version": CACHE_VERSION,
                    "server_url": self.server_url,
                    "refresh_token": token,
                    "created_at": datetime.datetime.now(
                        datetime.timezone.utc
                    ).isoformat(),
                }
            )
            # create or overwrite file, write-only, with permissions set atomically
            fd: int = os.open(
                tmp_path,
                os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
                CACHE_FILE_PERMISSIONS,
            )
            os.chmod(tmp_path, CACHE_FILE_PERMISSIONS)
            try:
                os.write(fd, data.encode())
            finally:
                os.close(fd)
            os.replace(tmp_path, path)
        except Exception as e:
            print(
                f"WARNING: Token cache write failed: {e}. "
                "To disable caching, pass token_cache_enabled=False to new_session()."
            )
            try:
                tmp_path.unlink(missing_ok=True)
            except OSError:
                pass
