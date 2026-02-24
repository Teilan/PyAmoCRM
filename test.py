import asyncio

from pyamocrm.Aut.token import Token
from pyamocrm.Aut.token_manager import TokenManager

asd = TokenManager(
    token=Token(
        client_id="...",
        client_secret="...",
        code="...",
        redirect_uri="...",
    ),
    subdomain="...",
)


print(asyncio.run(asd.creat_ouat_token(path="tokens")))
