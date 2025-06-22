from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from ..application.list_workflows_usecase import ListWorkflowsUseCase
from ..application.save_workflow_usecase import CreateWorkflowUseCase
from ..application.update_workflow_usecase import UpdateWorkflowUseCase
from ..application.get_workflow_by_name_usecase import GetWorkflowByNameUseCase
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
        
        if not all([name, description, status]):
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

class WorkflowGetByNameView(View):
    def get(self, request):
        name = request.GET.get('nameWorkflow')

        if not name:
            return JsonResponse(
                {'message': 'O parâmetro nameWorkflow é obrigatório.'},
                status=400
            )

        usecase = GetWorkflowByNameUseCase()
        workflow = usecase.execute(name)

        if workflow is None:
            return JsonResponse(
                {'message': f'Workflow com nome {name} não encontrado.'},
                status=404
            )

        data = {
            "id": str(workflow.id),
            "name": workflow.name,
            "description": workflow.description,
            "status": workflow.status,
            "created_at": workflow.created_at.isoformat(),
            "updated_at": workflow.updated_at.isoformat(),
        }

        return JsonResponse(data, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class WorkflowUpdateView(View):
    def put(self, request):
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Payload inválido. Envie um JSON válido.'}, status=400)

        workflow_name = payload.get('nameWorkflow')
        new_status = payload.get('new_status')

        if not workflow_name or not new_status:
            return JsonResponse(
                {'message': 'Campos obrigatórios: nameWorkflow e new_status.'},
                status=400
            )

        use_case = UpdateWorkflowUseCase()
        result = use_case.execute(workflow_name, new_status)

        if result is None:
            return JsonResponse({'message': 'Workflow não encontrado.'}, status=404)

        if result is False:
            return JsonResponse({'message': 'Erro ao atualizar workflow.'}, status=422)

        return JsonResponse({'message': 'Status do workflow atualizado com sucesso.'}, status=200)
            