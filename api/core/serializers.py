
from rest_framework import serializers
from .models import People, Film, Planet

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    username=serializers.CharField(required=True)

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields=[
            'title',
            'release_date'
        ]

    
class PeopleSerializer(serializers.ModelSerializer):
    films = FilmsSerializer(many=True, read_only=True)
    homeworld=serializers.CharField(source='homeworld.name', read_only=True)

    class Meta:
        model=People
        fields=[
            'name',
            'height',
            'mass',
            'hair_color',
            'gender',
            'dob',
            'img',
            'homeworld',
            'films'
        ]