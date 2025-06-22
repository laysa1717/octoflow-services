from ..infrastructure.repository import WorkflowRepository


class ListWorkflowsUseCase:
    def __init__(self):
        self.repository = WorkflowRepository()

    def execute(self):
        return self.repository.list_workflows()