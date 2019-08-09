from rest_framework import views, status, generics
from rest_framework.response import Response

from .serializers import (TaskSerializer)

from .models import Task


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
