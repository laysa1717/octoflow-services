from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class Workflow:
    id: UUID
    name: str
    description: str
    status: str
    trigger_type: str
    trigger_config: str
    created_at: datetime
    updated_at: datetime
