from pathlib import Path


class TokenStorage:
    # def __init__(self, path: str, type_save: str, data: dict):
    #     self.path = path
    #     self.type_save = type_save
    #     self.data = data

    def save(self, path: str, data: dict) -> None:
        base_path = Path(path)

        if not base_path.is_dir():
            raise ValueError(f"{path} is not a directory")

        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        (base_path / "access_token.txt").write_text(access_token)
        (base_path / "refresh_token.txt").write_text(refresh_token)

    async def load(path: str) -> None:
        base_path = Path(path)

        (base_path / "access_token.txt").read_text()
        (base_path / "refresh_token.txt").read_text()

        return base_path


# {
#   "token_type": "Bearer",
#   "expires_in": 86400,
#   "server_time": 1751621727,
#   "access_token": "xxxxxx",
#   "refresh_token": "xxxxx"
# }
