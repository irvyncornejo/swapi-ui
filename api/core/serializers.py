
from rest_framework import serializers
from .models import People, Film

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
    img=serializers.SerializerMethodField('get_img')
    height=serializers.SerializerMethodField('get_height')
    mass=serializers.SerializerMethodField('get_mass')

    class Meta:
        model=People
        fields=[
            'id',
            'name',
            'height',
            'mass',
            'hair_color',
            'gender',
            'dob',
            'homeworld',
            'films',
            'img'
        ]
    def get_img(self, obj):
        if not obj.img:
            return 'https://blog.spoongraphics.co.uk/wp-content/uploads/2012/star-wars/29.jpg'
        return obj.img

    def get_height(self, obj):
        return '{} cm'.format(obj.height)
    
    def get_mass(self, obj):
        if obj.mass and obj.mass != 'unknown':
            return f'{float(obj.mass)/100} Kg'
        return obj.mass
