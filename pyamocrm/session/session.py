import aiohttp


class Transport:
    def __init__(self):
        self._session: aiohttp.ClientSession | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self._session

    async def request(self, method, url, **kwargs):
        session = await self._get_session()

        async with session.request(method, url, **kwargs) as respons:
            data = await respons.json()
            return {"status": respons.status, "data": data}

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
