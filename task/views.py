from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (TaskSerializer)

from .models import Task

from users.models import CustomUser


class TaskListView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            task_id = kwargs.get('task_id')
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task with provided id not found"}, status=status.HTTP_404_NOT_FOUND)


class CreateTaskView(views.APIView):
    permission_classes = [IsAuthenticated, ]

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
                CustomUser.withdraw(customer.id, price)

                return Response({"success": "You've successfully created task"},
                                status=status.HTTP_201_CREATED)
            return Response({"permission_error": "Only customer can create task"},
                            status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            return Response({"error": "Database error"},
                            status=status.HTTP_400_BAD_REQUEST)
