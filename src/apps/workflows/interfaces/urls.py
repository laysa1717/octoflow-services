from django.urls import path
from .views import WorkflowListView, WorkflowCreateView, WorkflowUpdateView, WorkflowGetByNameView
from . import views

urlpatterns = [
    path('', WorkflowListView.as_view(), name='workflow-list'),
    path('create', WorkflowCreateView.as_view(), name='workflow-create'),
    path('update', WorkflowUpdateView.as_view(), name='workflow-update'),
    path('getWorkflowName/', WorkflowGetByNameView.as_view(), name='workflow-get-by-name'),
]
