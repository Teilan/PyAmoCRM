from session.session import Transport

from pyamocrm.models.amo_config import AmoConfig

from ..resources.leads_resource import LeadsResource


class AmoClient:
    def __init__(self, amo_config: AmoConfig):
        self._transport = Transport(...)
        self.amo_config = amo_config

        self.deals = LeadsResource(self._transport)
