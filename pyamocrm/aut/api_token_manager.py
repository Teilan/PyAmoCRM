import aiohttp

from .token import Token


class ApiTokenManager:
    def __init__(self, token: Token):
        self._token = token
        self.end_time = None

    async def _post_ouat_access_token(self):
        async with (
            aiohttp.ClientSession() as session,
            session.post(
                url="https://subdomain.amocrm.ru/oauth2/access_token",
            ) as response,
        ):
            response.text()
