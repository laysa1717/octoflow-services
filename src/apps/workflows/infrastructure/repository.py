from ..domain.entities import Workflow
from .models import WorkflowModel


class WorkflowRepository:
    def list_workflows(self):
        workflows = WorkflowModel.objects.all()

        if not workflows.exists():
            return None

        return [
            Workflow(
                id=w.id,
                name=w.name,
                description=w.description,
                status=w.status,
                created_at=w.created_at,
                updated_at=w.updated_at
            )
            for w in workflows
        ]

    def save_workflow(self, workflow_entity: Workflow):
        # no repository instancia a entidade
        # precisa instanciar o modelo da entidade(campos a serem salvos no banco)
        workflow_model = WorkflowModel(
            id=workflow_entity.id,
            name=workflow_entity.name,
            description=workflow_entity.description,
            status=workflow_entity.status,
        )
        workflow_model.save()

        return workflow_entity
    
    def get_workflow_by_name(self, name):
        try:
            workflow = WorkflowModel.objects.get(name=name)
        except WorkflowModel.DoesNotExist:
            return None

        return Workflow(
            id=workflow.id,
            name=workflow.name,
            description=workflow.description,
            status=workflow.status,
            created_at=workflow.created_at,
            updated_at=workflow.updated_at
        )

    def update_workflow_status(self, workflow_id, new_status):
        try:
            workflow = WorkflowModel.objects.get(id=workflow_id)
            workflow.status = new_status
            workflow.save()

            return True
        except WorkflowModel.DoesNotExist:
            return False