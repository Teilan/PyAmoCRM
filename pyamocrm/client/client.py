from session.session import Transport

from ..auth.token_manager import TokenManager
from ..resources.leads_resource import LeadsResource


class AmoClient:
    def __init__(self, token_manager: TokenManager):
        self._transport = Transport(...)
        self.amo_config = token_manager.config
        self.storage = token_manager.storage

        self.deals = LeadsResource(self._transport, self.amo_config, self.storage)
