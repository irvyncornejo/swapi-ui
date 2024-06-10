import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} {self.uuid}>'

    def __str__(self) -> str:
        return f'{self.uuid}'


class User(AbstractBaseUser, PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email

class Films(AbstractBaseModel):
    title=models.CharField(max_length=100)
    episode_id=models.CharField()
    opening_crawl=models.CharField()
    director=models.CharField()
    producer=models.CharField()
    release_date=models.CharField()
    external_reference=models.IntegerField(max_length=10)

class Planets(AbstractBaseModel):
    name=models.CharField(max_length=100)
    rotation_period=models.CharField()
    orbital_period=models.CharField()
    diameter=models.CharField()
    climate=models.CharField()
    gravity=models.CharField()
    terrain=models.CharField()
    surface_water=models.CharField()
    population=models.CharField()

class Species(AbstractBaseModel):
    name=models.CharField(max_length=100)
    classification=models.CharField()
    designation=models.CharField()
    average_height=models.CharField()
    skin_colors=models.CharField()
    hair_colors=models.CharField()
    eye_colors=models.CharField()
    average_lifespan=models.CharField()
    homeworld=models.CharField()
    language=models.CharField()

class People(AbstractBaseModel):
    name=models.CharField(max_length=100)
    age=models.CharField()
    height=models.CharField()
    mass=models.CharField()
    hairColor=models.CharField()
    gender=models.CharField()
    homeworld=models.CharField()
    dob=models.CharField()
    films=models.ManyToManyField('Films')


