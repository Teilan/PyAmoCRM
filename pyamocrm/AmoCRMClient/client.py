from AmoCRMSession.session import Transport
from Aut.amo_config import AmoConfig

from .Leads.leads_resource import LeadsResource


class AmoClient:
    def __init__(self, amo_config: AmoConfig):
        self._transport = Transport(...)
        self.amo_config = amo_config

        self.deals = LeadsResource(self._transport)
