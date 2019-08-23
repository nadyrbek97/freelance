from django.urls import path

from .views import (TaskListView,
                    CreateTaskView,
                    TaskDetailView,
                    GetCustomerTaskView)

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task-list'),
    path('create/', CreateTaskView.as_view(), name='task-create'),
    path('<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    path('get/', GetCustomerTaskView.as_view(), name='task-get')
]
