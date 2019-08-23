from django.shortcuts import reverse

from rest_framework.test import APITestCase, APIClient

from .models import CustomUser


class UserTest(APITestCase):

    user_data = {
        "username": "test_user",
        "password": "test123"
    }

    user_registration_data = {
        "username": "test_user_2",
        "email": "test@email.com",
        "role": 1,
        "password": "test123",
        "password_repeat": "test123"
    }

    def setUp(self) -> None:
        self.client = APIClient()
        self.login_url = reverse('user-login')
        self.registration_url = reverse('user-registration')
        self.test_user = CustomUser.objects.create_user(username="test_user",
                                                        password="test123",
                                                        email="customer@gmail.com",
                                                        role=1,
                                                        balance=500)

    def test_user_registration(self):

        response = self.client.post(self.registration_url,
                                    self.user_registration_data)

        self.assertEqual(response.status_code, 201)

    def test_user_login(self):

        response = self.client.post(self.login_url,
                                    self.user_data)

        self.assertEqual(response.status_code, 200)
