import asyncio

from pyamocrm.auth.token_manager import TokenManager
from pyamocrm.auth.token_storage import TokenStorage
from pyamocrm.client import AmoClient

manager = TokenManager(
    client_id="...",
    client_secret="...",
    redirect_uri="...",
    subdomain="...",
    storage=TokenStorage(path="..."),
)

asyncio.run(manager.create_oauth_token(code="..."))


client = AmoClient(manager)

# await client.contacts.create(...)
# await client.contacts.list(...)
# await client.leads.create(...)
# await client.leads.list(...)
