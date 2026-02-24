from dataclasses import asdict

import aiohttp

from .token import Token
from .token_storage import TokenStorage


class TokenManager:
    def __init__(self, subdomain: str, token: Token):
        self._token: Token = token
        self._storage: TokenStorage = TokenStorage()
        self.end_time = None
        self.subdomen: str = subdomain

    async def creat_ouat_token(
        self,
        path: str,
    ) -> None:
        headers = {"Content-Type": "application/json"}
        data = asdict(self._token)

        async with (
            aiohttp.ClientSession() as session,
            session.post(
                url=f"https://{self.subdomen}.amocrm.ru/oauth2/access_token",
                headers=headers,
                json=data,
            ) as response,
        ):
            try:
                respons_json = await response.json()
                if response.status == 400:
                    raise ValueError(respons_json)
                else:
                    self._storage.save(path=path, data=respons_json)
            except Exception as e:
                raise ValueError("Error saving token") from e

    async def get_valid_token(self):
        pass
