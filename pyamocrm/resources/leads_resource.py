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

    async def _fetch_paginated(self, headers):
        leads = []
        page = 1
        params = {
            "page": page,
            "limit": 250,
            "with": "contacts",
            "order[updated_at]": "asc",
        }

        while True:
            response = await self._transport.request(
                method="get",
                url=f"https://{self.amo_config.subdomain}.amocrm.ru/api/v4/leads",
                params=params,
                headers=headers,
            )

            if response.status == 400:
                break

            params += 1
            lead = self._map_lead(response)
            leads.append(lead)

        return leads

    async def all(self) -> dict[Leads]:
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = self._fetch_paginated(headers)

        return response

    async def get_by_id(self, lead_id: int) -> Leads:
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = await self._transport.request(
            method="get",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru/api/v4/leads/{lead_id}",
            headers=headers,
        )

        lead = self._map_lead(response)
        return lead

    async def add(self, lead: dict) -> Leads:  # POST /api/v4/leads
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = await self._transport.request(
            method="post",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru//api/v4/leads",
            headers=headers,
            json=[lead],
        )

        if response.status == 400:
            return (
                "Uncorrected data was transmitted. "
                "Details are available in the response body."
            )

        lead_id = response[0].get("id")

        return await self.get_by_id(lead_id)

    async def add_many(self, leads: list[dict]) -> list[Leads]:
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = await self._transport.request(
            method="post",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru//api/v4/leads",
            headers=headers,
            json=leads,
        )

        if response.status == 400:
            return (
                "Uncorrected data was transmitted. "
                "Details are available in the response body."
            )

        created_leads = []
        for lead_data in response:
            lead_id = lead_data.get("id")
            created_leads.append(await self.get_by_id(lead_id))

        return created_leads

    async def add_complex(): ...  # POST /api/v4/leads/complex

    async def update(self, lead_id: int, lead: dict) -> Leads:
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = await self._transport.request(
            method="patch",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru//api/v4/leads/{lead_id}",
            headers=headers,
            json=lead,
        )

        if response.status == 400:
            return (
                "Uncorrected data was transmitted. "
                "Details are available in the response body."
            )

        return await self.get_by_id(lead_id)

    async def update_many(self, leads: list[dict]) -> list[Leads]:
        accses_token = self.storage.upload_access_token()

        headers = {
            "Authorization": f"Bearer {accses_token}",
            "Content-Type": "application/json",
        }

        response = await self._transport.request(
            method="patch",
            url=f"https://{self.amo_config.subdomain}.amocrm.ru//api/v4/leads",
            headers=headers,
            json=leads,
        )

        if response.status == 400:
            return (
                "Uncorrected data was transmitted. "
                "Details are available in the response body."
            )

        updated_leads = []
        for lead_data in response:
            updated_lead_id = lead_data.get("id")
            updated_leads.append(await self.get_by_id(updated_lead_id))

        return updated_leads
