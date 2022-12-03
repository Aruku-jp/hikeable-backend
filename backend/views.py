from django.contrib.auth.models import User, Group
from .models import Trail
from backend.serializers import UserSerializer, GroupSerializer, TrailSerializer

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def TrailList (request):
    if request.method == 'GET':
        TrailData = Trail.objects.all()
        Serializer = TrailSerializer(TrailData, many=True)
        return JsonResponse(Serializer.data, safe=False)

@api_view(['GET'])
def TrailDetail (request, pk):
    try:
        TrailData = Trail.objects.filter(id=pk)
    except Trail.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Serializer = TrailSerializer(TrailData, many=True)
        return JsonResponse(Serializer.data, safe=False)