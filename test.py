import asyncio

from pyamocrm.Aut.token_manager import TokenManager
from pyamocrm.Aut.token_storage import TokenStorage

manager = TokenManager(
    client_id="...",
    client_secret="...",
    redirect_uri="...",
    subdomain="...",
    storage=TokenStorage(path="..."),
)

asyncio.run(manager.create_oauth_token(code="..."))


# client = AmoCRMClient(manager)

# await client.contacts.create(...)
# await client.contacts.list(...)
# await client.leads.create(...)
# await client.leads.list(...)
