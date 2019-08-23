from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.reverse import reverse as rest_reverse
from rest_framework.permissions import (AllowAny, )
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate, login

from .serializers import (UserRegistrationSerializer,
                          UserLoginSerializer)
from .models import CustomUser


@api_view(['GET'])
def api_root_view(request, format=None):
    return Response({
        'User Register': rest_reverse('user-registration', request=request, format=format),
        'User Log In': rest_reverse('user-login', request=request, format=format),
        'Task List': rest_reverse('task-list', request=request, format=format),
        'Task Create': rest_reverse('task-create', request=request, format=format),
        'Get Task': rest_reverse('task-get', request=request, format=format)
    })


class UserRegistrationView(views.APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['password'] != request.data['password_repeat']:
                return Response({'error': 'passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            user = CustomUser.objects.create_user(**serializer.validated_data)
            login(request, user=user)
            return Response({'successful': "You've registered successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(views.APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user:
                login(request, user)
                return Response({"success": "You've logged in successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "authentication error"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
