from django.urls import path

from .views import (TaskListView,)

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task-list')
]