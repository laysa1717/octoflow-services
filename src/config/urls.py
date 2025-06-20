
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def health_check(request):
    return JsonResponse(
        {"message": "API rodando na porta 8000 - status code 200"},
        status=200
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check),
]
