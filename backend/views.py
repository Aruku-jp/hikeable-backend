from django.contrib.auth.models import User, Group
from .models import Trail, TrailComment
from backend.serializers import UserSerializer, GroupSerializer, TrailSerializer, TrailCommentSerializer

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

@api_view(['GET', 'POST'])
def TrailList (request):
    if request.method == 'GET':
        TrailData = Trail.objects.all()
        Serializer = TrailSerializer(TrailData, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        TrailData = JSONParser().parse(request)
        Serializer = TrailSerializer(data=TrailData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def TrailDetail (request, pk):
    try:
        TrailData = Trail.objects.filter(id=pk)
    except Trail.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Serializer = TrailSerializer(TrailData, many=True)
        return JsonResponse(Serializer.data, safe=False)
    
    elif request.method == 'PUT':
        OldTrailData = Trail.objects.get(id=pk)
        NewTrailData = JSONParser().parse(request)
        Serializer = TrailSerializer(OldTrailData, data=NewTrailData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        TrailData.delete()
        return JsonResponse({'message': 'The listing was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def TrailCommentList (request):
    if request.method == 'GET':
        TrailCommentData = TrailComment.objects.all()
        Serializer = TrailCommentSerializer(TrailCommentData, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        TrailCommentData = JSONParser().parse(request)
        Serializer = TrailCommentSerializer(data=TrailCommentData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)