from django.views.decorators.csrf import csrf_exempt

from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import (TaskSerializer)

from .models import Task

from users.models import CustomUser


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskView(views.APIView):

    def post(self, request):
        try:
            data = request.data
            title = data['title']
            description = data['description']
            price = data['price']
            # user
            customer = request.user

            Task.objects.create(title=title,
                                description=description,
                                price=price,
                                customer=customer)

            return Response({"success": "You've successfully created task"},
                            status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"error": "Database error"},
                            status=status.HTTP_400_BAD_REQUEST)
