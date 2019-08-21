from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from users.models import CustomUser


class TaskTest(APITestCase):

    customer_data = {
        "username": "customer",
        "password": "test123"
    }

    executor_data = {
        "username": "executor",
        "password": "test123"
    }

    login_url = reverse('user-login')

    def setUp(self):
        self.client = APIClient()
        self.task_create_url = reverse('task-create')
        self.test_customer = CustomUser.objects.create_user(username="customer",
                                                            password="test123",
                                                            email="customer@gmail.com",
                                                            role=1,
                                                            balance=500)
        self.test_executor = CustomUser.objects.create_user(username="executor",
                                                            password="test123",
                                                            email="executor@gmail.com",
                                                            role=2,
                                                            balance=500)

    def test_task_list(self):
        test_url = reverse('task-list')
        response = self.client.get(test_url)

        self.assertEqual(response.status_code, 200)

    def test_task_create_success(self):

        data = {
            "title": "test title",
            "description": "this is description",
            "price": 500
        }
        # login customer
        self.client.post(self.login_url, self.customer_data)

        response = self.client.post(self.task_create_url, data)

        self.assertEqual(response.status_code, 201)

    def test_task_create_key_error(self):

        data = {
            "title": "test title",
            "description": "this is description",
            "wrong_field_price": 500
        }
        # login customer
        self.client.post(self.login_url, self.customer_data)

        response = self.client.post(self.task_create_url, data)

        self.assertEqual(response.status_code, 400)

    def test_task_create_forbidden(self):

        data = {
            "title": "test title",
            "description": "this is description",
            "price": 500
        }
        # login executor
        self.client.post(self.login_url, self.executor_data)

        response = self.client.post(self.task_create_url, data)

        self.assertEqual(response.status_code, 403)
