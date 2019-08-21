from django.urls import path

from .views import (TaskListView,
                    CreateTaskView)

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task-list'),
    path('create/', CreateTaskView.as_view(), name='task-create')
]
