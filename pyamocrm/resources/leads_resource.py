from dataclasses import fields

from session.session import Transport

from ..auth.token_storage import TokenStorage
from ..models.amo_config import AmoConfig
from ..models.leads import Leads, LeadsEmbedded


class LeadsResource:
    def __init__(
        self, transport: Transport, amo_config: AmoConfig, storage: TokenStorage
    ):
        self._transport = transport
        self.amo_config = amo_config
        self.storage = storage

    def _map_lead(self, data: dict[str, object]) -> Leads:
        embedded_raw = data.get("_embedded") or {}
        embedded = LeadsEmbedded(
            tags=embedded_raw.get("tags"),
            companies=embedded_raw.get("companies"),
        )

        lead_kwargs = {
            f.name: data.get(f.name) for f in fields(Leads) if f.name != "_embedded"
        }

        return Leads(**lead_kwargs, _embedded=embedded)

    def _paginate(self): ...

    def _fetch(self): ...

    async def all(self) -> list:
        accses_token = self.storage.upload_access_token()
        leads = []

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        params = {
            "page": 1,
            "limit": 250,
            "with": "contacts",
            "order[updated_at]": "asc",
        }

        response = self._transport.request(
            method="get",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru/api/v4/leads",
            params=params,
            headers=headers,
        )

        return response

    async def get_by_id(self, lead_id: int):
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = self._transport.request(
            method="get",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru/api/v4/leads/{lead_id}",
            headers=headers,
        )

        lead = self._map_lead(response)

        return lead

    async def add(): ...

    async def add_complex(): ...

    async def update(): ...
