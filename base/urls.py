# urls.py
from django.urls import path
from . import views
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('', views.taskList, name='tasks'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
]
