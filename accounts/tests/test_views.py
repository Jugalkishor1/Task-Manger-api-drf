from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterViewTest(APITestCase):

    def test_user_registration_success(self):
        url = reverse("register")
        data = {
            "name": "Jugal",
            "email": "testuser@example.com",
            "password": "Test@1234"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "User created successfully")
        self.assertEqual(response.data['data']['email'], data["email"])

    def test_user_registration_failure(self):
        url = reverse("register")
        data = {
            "name": "Jugal",
            "email": "",
            "password": "Test@1234"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            name="Jugal",
            email="test@example.com",
            password="Test@1234"
        )

    def test_login_success(self):
        url = reverse('login')
        data = {
            "email": "test@example.com",
            "password": "Test@1234"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
