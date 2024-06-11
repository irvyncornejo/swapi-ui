
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APIClient


class TokenUserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'test',
            'password': '$er44444',
            'email': 'testuser@example.com'
        }
        self.user=User(
            username=self.user_data['username']
        )
        self.user.set_password(self.user_data['password'])
        self.user.email=self.user_data['email']
        self.user.save()

        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_token_user(self):
        response = self.client.get('/api/people')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
