from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'firebase_uid', 'email']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'name', 'prefecture', 'latitude', 'longitude', 'length', 'difficulty', 'photo_url', 'map_url']
    
class TrailCommentSerializer(ModelSerializer):
    class Meta:
        model = TrailComment
        fields = ['id', 'user', 'trail_id', 'comment', 'date']

class TrailLikeSerializer(ModelSerializer):
    class Meta:
        model = TrailLike
        fields = ['id', 'user', 'trail_id', 'like']

class TrailCompletionSerializer(ModelSerializer):
    class Meta:
        model = TrailCompletion
        fields = ['id', 'user', 'trail_id', 'completion', 'date']