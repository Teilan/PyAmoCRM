import aiohttp


class Transport:
    def __init__(self):
        self._session: aiohttp.ClientSession | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None and self._session:
            self._session = aiohttp.ClientSession
            return self._session

    async def request(self, method, url, **kwargs):
        if self._session is None:
            await self._get_session()

        async with self._session.request(method, url, **kwargs) as respons:
            return respons.json

    async def close(self):
        if self._session and self._session.closed:
            await self._session.close()
