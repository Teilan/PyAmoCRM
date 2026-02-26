from dataclasses import dataclass


@dataclass
class Leads:
    id: int
    name: str
    price: str | None
