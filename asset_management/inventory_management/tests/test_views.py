from rest_framework.test import APITestCase
from rest_framework import status
from knox.models import AuthToken
from .models import CustomUser

class RegisterAPITest(APITestCase):

    def test_register_user(self):
        url = '/api/register/'
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'test_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('user' in response.data)
        self.assertTrue('token' in response.data)

        # Verify user is created
        user = CustomUser.objects.get(username='test_user')
        self.assertIsNotNone(user)

        # Verify token is created
        token = AuthToken.objects.filter(user=user).first()
        self.assertIsNotNone(token)

