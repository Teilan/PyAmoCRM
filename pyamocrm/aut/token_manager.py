from dataclasses import asdict

import aiohttp

from .amo_config import AmoConfig
from .token_storage import TokenStorage


class TokenManager:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        subdomain: str,
        storage: TokenStorage,
    ):
        self.config = AmoConfig(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            subdomain=subdomain,
        )
        self.storage = storage

    async def create_oauth_token(self, code: str) -> None:
        grant_type: str = "authorization_code"

        headers = {"Content-Type": "application/json"}
        data = asdict(self.config)
        data["grant_type"] = grant_type
        data["code"] = code

        async with (
            aiohttp.ClientSession() as session,
            session.post(
                url=f"https://{data.get('subdomen')}.amocrm.ru/oauth2/access_token",
                headers=headers,
                json=data,
            ) as response,
        ):
            try:
                respons_json = await response.json()
                if response.status == 400:
                    raise ValueError(respons_json)
                else:
                    self.storage.save(data=respons_json)
            except Exception as e:
                raise ValueError("Error saving token") from e

    async def get_valid_token(self):
        pass
