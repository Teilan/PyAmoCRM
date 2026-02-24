from dataclasses import dataclass


@dataclass
class Token:
    client_id: str
    client_secret: str
    code: str
    redirect_uri: str  # может тут стоит создать отдельный обьект для чего то, но хз
    grant_type: str = "authorization_code"
