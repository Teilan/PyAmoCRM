from pathlib import Path


class TokenStorage:
    ACCESS_TOKEN_FILENAME = "access_token.txt"
    REFRESH_TOKEN_FILENAME = "refresh_token.txt"

    def __init__(self, path: str):
        self.path = Path(path)

    def _ensure_storage_dir(self) -> Path:
        if not self.path.is_dir():
            raise ValueError(f"{self.path} is not a directory")
        return self.path

    def _validate_token(self, token: str, name: str) -> str:
        if not isinstance(token, str) or not token:
            raise ValueError(f"{name} must be a non-empty string")
        return token

    def _write_tokens(self, access_token: str, refresh_token: str) -> None:
        base_path = self._ensure_storage_dir()
        validated_access_token = self._validate_token(access_token, "access_token")
        validated_refresh_token = self._validate_token(refresh_token, "refresh_token")

        (base_path / self.ACCESS_TOKEN_FILENAME).write_text(
            validated_access_token, encoding="utf-8"
        )
        (base_path / self.REFRESH_TOKEN_FILENAME).write_text(
            validated_refresh_token, encoding="utf-8"
        )

    def _read_tokens(self) -> tuple[str, str]:
        base_path = self._ensure_storage_dir()
        access_token_path = base_path / self.ACCESS_TOKEN_FILENAME
        refresh_token_path = base_path / self.REFRESH_TOKEN_FILENAME

        if not access_token_path.is_file():
            raise FileNotFoundError(f"{access_token_path} was not found")
        if not refresh_token_path.is_file():
            raise FileNotFoundError(f"{refresh_token_path} was not found")

        access_token = access_token_path.read_text(encoding="utf-8")
        refresh_token = refresh_token_path.read_text(encoding="utf-8")
        return access_token, refresh_token

    def save(self, data: dict[str, object]) -> None:
        access_token = self._validate_token(data.get("access_token"), "access_token")
        refresh_token = self._validate_token(data.get("refresh_token"), "refresh_token")
        self._write_tokens(access_token=access_token, refresh_token=refresh_token)

    def unload(self) -> tuple[str, str]:
        return self._read_tokens()

    def load(self, access_token: str, refresh_token: str) -> None:
        self._write_tokens(access_token=access_token, refresh_token=refresh_token)


# {
#   "token_type": "Bearer",
#   "expires_in": 86400, через сколько истекает токен
#   "server_time": 1751621727,
#   "access_token": "xxxxxx",
#   "refresh_token": "xxxxx"
# }
