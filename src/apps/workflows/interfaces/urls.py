from django.urls import path
from .views import WorkflowListView, WorkflowCreateView
from . import views

urlpatterns = [
    path('', WorkflowListView.as_view(), name='workflow-list'),
    path('create', WorkflowCreateView.as_view(), name='workflow-create'),

]
