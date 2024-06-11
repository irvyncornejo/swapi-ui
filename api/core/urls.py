from django.urls import path


from .api import (
    LoginView,
    RegisterView,
    ProfileView,
    PeopleView,
    SearchView
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('people', PeopleView.as_view(), name='people'),
    path('people/search', SearchView.as_view(), name='search')
]