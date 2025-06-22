from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class Workflow:
    id: UUID
    name: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
