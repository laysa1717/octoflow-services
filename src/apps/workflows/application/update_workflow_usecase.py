from ..infrastructure.repository import WorkflowRepository
from ..domain.entities import Workflow
from .get_workflow_by_name_usecase import GetWorkflowByNameUseCase

class UpdateWorkflowUseCase:
    def __init__(self):
        self.repository = WorkflowRepository()
    
    def execute(self, nameWorkflow, newStatus):
        get_workflow_usecase = GetWorkflowByNameUseCase()
        workflow = get_workflow_usecase.execute(nameWorkflow)

        if not workflow:
            return None  # Ou lança uma Exception se quiser

        success = self.repository.update_workflow_status(workflow.id, newStatus)
        return success
