from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    username=serializers.CharField(required=True)

    
