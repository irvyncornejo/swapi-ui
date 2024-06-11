import uuid
from django.db import models


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.id}'



class Film(AbstractBaseModel):
    title=models.CharField(max_length=100)
    episode_id=models.CharField(max_length=20)
    opening_crawl=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    producer=models.CharField(max_length=20)
    release_date=models.DateField()
    external_reference=models.IntegerField()
    def __str__(self):
        return self.title

class Planet(AbstractBaseModel):
    name=models.CharField(max_length=100)
    rotation_period=models.CharField(max_length=20)
    orbital_period=models.CharField(max_length=20)
    diameter=models.CharField(max_length=20)
    climate=models.CharField(max_length=20)
    gravity=models.CharField(max_length=20)
    terrain=models.CharField(max_length=20)
    surface_water=models.CharField(max_length=20)
    population=models.CharField(max_length=20)
    external_reference=models.IntegerField()

    def __str__(self):
        return self.name

class People(AbstractBaseModel):
    name=models.CharField(max_length=100)
    height=models.CharField(max_length=10)
    mass=models.CharField(max_length=10)
    hair_color=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    homeworld=models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='planet', null=True)
    dob=models.CharField(max_length=10)
    films=models.ManyToManyField(Film, related_name='films', null=True)
    img=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
