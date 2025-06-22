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
            trigger_type= workflow_entity.trigger_type,
            trigger_config= workflow_entity.trigger_config
        )
        workflow_model.save()

        return workflow_entity