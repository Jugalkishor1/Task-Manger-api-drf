from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),  # This is for List and create tasks
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),  # Retrieve, update, delete task
]
