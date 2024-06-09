from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, requests, format=None):
        user = get_object_or_404(User, username=requests.data['username'])
        if user.check_password(requests.data['password']):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': user.username
            })
        return Response({
            'error': 'Wrong credentials'
        }, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(ObtainAuthToken):
    def post(self, requests, format=None):
        serializer = UserSerializer(data=requests.data)
        if serializer.is_valid():
            try:
                user=User.objects.get(username=serializer.data['username'])
                return Response({
                    'error': 'User already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                user=User(
                    username=serializer.data['username']
                )
                user.set_password(serializer.data['password'])
                user.email=serializer.data['email']
                user.save()
                token = Token.objects.create(user=user)
                return Response({
                    'token': token.key,
                    'user': user.username
                }, status=status.HTTP_201_CREATED)
        return Response({
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def post(self, requests, format=None):
        return Response({})
