from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..models import People

from .setUp import SetUp

class UserTestCase(TestCase, SetUp):
    def setUp(self) -> None:
        #TODO CHANGE TO FAKER
        self.user_data = {
            'username': 'test',
            'password': '$er44444',
            'email': 'testuser@example.com'
        }


    def test_user_creation(self):
        user=User(
            username=self.user_data['username']
        )
        user.set_password(self.user_data['password'])
        user.email=self.user_data['email']
        user.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, self.user_data['username'])

class PeopleTestCase(TestCase, SetUp):
    def setUp(self) -> None:
        super().__init__()
        self._run()

    def test_people_creation(self):
        people = People.objects.create(
            name="Luke Skywalker",
            height="172",
            mass="77",
            hair_color="blond",
            dob="19BBY",
            gender="male",
            img=''
        )
        people.homeworld = self.planet
        people.films.set([self.film])
        people.save()
        self.assertIsInstance(people, People)
        self.assertEqual(people.name, "Luke Skywalker")
