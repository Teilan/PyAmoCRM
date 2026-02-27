from dataclasses import dataclass
from typing import Any


@dataclass
class LeadsEmbedded:
    tags: dict | None = None
    companies: dict | None = None


@dataclass
class Leads:
    id: int
    name: str
    price: int | None
    responsible_user_id: int
    group_id: int | None = None
    status_id: int | None = None
    pipeline_id: int | None = None
    loss_reason_id: int | None = None
    source_id: int | None = None
    created_by: int | None = None
    updated_by: int | None = None
    closed_at: int | None = None
    created_at: int | None = None
    updated_at: int | None = None
    closest_task_at: int | None = None
    is_deleted: bool | None = None
    custom_fields_values: list[dict[str, Any]] | None = None
    score: int | None = None
    account_id: int | None = None
    labor_cost: int | None = None
    is_price_modified_by_robot: bool | None = None
    _embedded: LeadsEmbedded
