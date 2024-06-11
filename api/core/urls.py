from django.urls import path
from .serializers import PeopleSerializer
from .models import People

from .api import (
    LoginView,
    RegisterView,
    ProfileView,
    PeopleView
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('people', PeopleView.as_view(), name='people')
]