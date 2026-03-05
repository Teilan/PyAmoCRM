from session.session import Transport

from ..models.amo_config import AmoConfig


class LeadsResource:
    def __init__(self, transport: Transport, amo_config: AmoConfig):
        self._transport = transport
        self.amo_config = amo_config

    async def all(self) -> list:
        """
        Описание
        Метод позволяет получить список сделок в аккаунте.

        Ограничения
        Метод доступен в соответствии с правами пользователя.
        """

        headers = {
            "Authorization": f"Bearer {''}",
            "Content-Type": "application/json",
        }

        params = {
            "page": 1,
            "limit": 50,
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
