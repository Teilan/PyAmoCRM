from dataclasses import dataclass


@dataclass
class AmoConfig:
    client_id: str
    client_secret: str
    subdomain: str
    redirect_url: str
