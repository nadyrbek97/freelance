from rest_framework import serializers

from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password')
