from ..infrastructure.repository import WorkflowRepository


class GetWorkflowByNameUseCase:
    def __init__(self):
        self.repository = WorkflowRepository()

    def execute(self, name):
        return self.repository.get_workflow_by_name(name)
