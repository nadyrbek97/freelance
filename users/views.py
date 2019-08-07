from rest_framework import views, status
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout

from .serializers import (UserRegistrationSerializer)
from .models import CustomUser


class UserRegistrationView(views.APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['password'] != request.data['password_repeat']:
                return Response({'error': 'passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            user = CustomUser.objects.create_user(**serializer.validated_data)
            login(request, user=user)
            return Response({'successful': "You've registered successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

