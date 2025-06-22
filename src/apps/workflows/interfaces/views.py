from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from ..application.list_workflows_usecase import ListWorkflowsUseCase
from ..application.save_workflow_usecase import CreateWorkflowUseCase
import json



class WorkflowListView(View):
    def get(self, request):
        usecase = ListWorkflowsUseCase()
        workflows = usecase.execute()

        if workflows is None:
            return JsonResponse(
                {"message": "Não há workflows cadastrados"},
                status=404
            )

        data = [
            {
                "id": str(w.id),
                "name": w.name,
                "description": w.description,
                "status": w.status,
                "created_at": w.created_at.isoformat(),
                "updated_at": w.updated_at.isoformat(),
            }
            for w in workflows
        ]

        return JsonResponse(data, safe=False, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class WorkflowCreateView(View):
     def post(self, request):
        saveUsecase = CreateWorkflowUseCase();
         
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {'message': 'Payload inválido. Envie um JSON válido.'}, 
                status=400
            )

        name = payload.get('name')
        description = payload.get('description')
        status = payload.get('status')
        trigger_type = payload.get('trigger_type')
        trigger_config = payload.get('trigger_config')

        if not all([name, description, status, trigger_type, trigger_config]):
            return JsonResponse(
                {'message': 'Campos obrigatórios: name, description e status.'},
                status=400
            )
        try:
            saveResponse = saveUsecase.execute(payload)
            if saveResponse:
                return JsonResponse(
                    {'message': 'Workflow criado com sucesso.'},
                    status=201
                )
        except json.JSONDecodeError:
            return JsonResponse(
                {'message': 'Erro ao salvar dados no banco de dados.'}, 
                status=422
            )        

       
