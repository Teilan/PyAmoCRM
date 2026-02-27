from AmoCRMSession.session import Transport


class LeadsResource:
    def __init__(self, transport: Transport):
        self._transport = transport

    async def all(self): ...
