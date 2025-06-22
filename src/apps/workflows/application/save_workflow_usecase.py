from uuid import uuid4
from datetime import datetime
from ..infrastructure.repository import WorkflowRepository
from ..domain.entities import Workflow


class CreateWorkflowUseCase:
    def __init__(self):
        self.repository = WorkflowRepository()

    def execute(self, payload):
        workflow = Workflow(
            id=uuid4(),
            name=payload.get('name'),
            description=payload.get('description'),
            status=payload.get('status'),
            trigger_type= payload.get('trigger_type'),
            trigger_config = payload.get('trigger_config'),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        self.repository.save_workflow(workflow)

        return workflow
