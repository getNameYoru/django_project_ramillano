from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # List all tasks
    path('create/', views.task_create, name='task_create'),  # Create a new task
    path('update/<int:task_id>/', views.task_update, name='task_update'),  # Update a task
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),  # Delete a task
]