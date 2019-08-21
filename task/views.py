from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (TaskSerializer)

from .models import Task


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskView(views.APIView):

    def post(self, request):
        try:
            if request.user.role == 1:
                customer = request.user

                data = request.data
                title = data['title']
                description = data['description']
                price = data['price']

                Task.objects.create(title=title,
                                    description=description,
                                    price=price,
                                    customer=customer)

                return Response({"success": "You've successfully created task"},
                                status=status.HTTP_201_CREATED)
            return Response({"permission_error": "Only customer can create task"},
                            status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            return Response({"error": "Database error"},
                            status=status.HTTP_400_BAD_REQUEST)
