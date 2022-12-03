from django.contrib.auth.models import User, Group
from .models import Trail
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'name', 'prefecture', 'latitude', 'longitude', 'length', 'difficulty', 'photo_url', 'map_url']