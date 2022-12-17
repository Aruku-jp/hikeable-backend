import json
from django.contrib.auth.models import User, Group
from django.shortcuts import HttpResponse
from .models import *
from backend.serializers import *

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from django.core import serializers
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
def TrailList(request):
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
def TrailDetail(request, pk):
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
def TrailCommentList(request):
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


@api_view(['GET'])
def TrailCommentDetail(request, pk):
    try:
        TrailCommentData = TrailComment.objects.filter(trail_id=pk)
    except TrailComment.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = TrailCommentSerializer(TrailCommentData, many=True)
        return JsonResponse(Serializer.data, safe=False)


@api_view(['GET', 'POST'])
def TrailLikeList(request):
    if request.method == 'GET':
        TrailLikeData = TrailLike.objects.all()
        Serializer = TrailLikeSerializer(TrailLikeData, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        TrailLikeData = JSONParser().parse(request)
        Serializer = TrailLikeSerializer(data=TrailLikeData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TrailLikeGet(request, pk):
    try:
        TrailLikeData = TrailLike.objects.filter(trail_id=pk)
    except TrailLike.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = TrailLikeSerializer(TrailLikeData, many=True)
        return JsonResponse(Serializer.data, safe=False)


@api_view(['PUT'])
def TrailLikePut(request, pk):
    if request.method == 'PUT':
        OldLikeData = TrailLike.objects.get(id=pk)
        NewLikeData = JSONParser().parse(request)
        Serializer = TrailLikeSerializer(OldLikeData, data=NewLikeData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def TrailCompletionList(request):
    if request.method == 'GET':
        TrailCompletionData = TrailCompletion.objects.all()
        Serializer = TrailCompletionSerializer(TrailCompletionData, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        TrailCompletionData = JSONParser().parse(request)
        Serializer = TrailCompletionSerializer(data=TrailCompletionData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TrailCompletionGet(request, pk):
    try:
        TrailCompletionData = TrailCompletion.objects.filter(trail_id=pk)
    except TrailLike.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = TrailCompletionSerializer(TrailCompletionData, many=True)
        return JsonResponse(Serializer.data, safe=False)


@api_view(['PUT'])
def TrailCompletionPut(request, pk):
    if request.method == 'PUT':
        OldCompletionData = TrailCompletion.objects.get(id=pk)
        NewCompletionData = JSONParser().parse(request)
        Serializer = TrailCompletionSerializer(
            OldCompletionData, data=NewCompletionData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        Users = Account.objects.all()
        Serializer = AccountSerializer(Users, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        UserID = JSONParser().parse(request)
        Serializer = AccountSerializer(data=UserID)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get(request, uid: str):
    try:
        User = Account.objects.filter(firebase_uid=uid)
    except Account.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = AccountSerializer(User, many=True)
        return JsonResponse(Serializer.data, safe=False)


@api_view(['GET', 'POST'])
def TrailMessageList(request):
    if request.method == 'GET':
        TrailMessageData = TrailMessage.objects.all()
        Serializer = TrailMessageSerializer(TrailMessageData, many=True)
        return JsonResponse(Serializer.data, safe=False)

    elif request.method == 'POST':
        TrailMessageData = JSONParser().parse(request)
        Serializer = TrailMessageSerializer(data=TrailMessageData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TrialMessageGet(request, pk):
    try:
        TrailMessageData = TrailMessage.objects.filter(trail_id=pk)
    except TrailMessage.DoesNotExist:
        return JsonResponse({'message': 'The listing does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = TrailMessageSerializer(TrailMessageData, many=True)
        return JsonResponse(Serializer.data, safe=False)


@api_view(['PUT'])
def TrailMessagePut(request, pk):
    if request.method == 'PUT':
        OldMessageData = TrailMessage.objects.get(id=pk)
        NewMessageData = JSONParser().parse(request)
        Serializer = TrailMessageSerializer(
            OldMessageData, data=NewMessageData)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def UserBadgeList(request, pk):
    try: 
        BadgesData = Badge.objects.filter(user=pk)
    except Badge.DoesNotExist:
        return JsonResponse({'message': 'This user has no badges'}, stastatus=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Serializer = BadgeSerializer(BadgesData, many=True)
        return JsonResponse(Serializer.data, safe=False)
    
    elif request.method == 'POST':
        NewBadge = JSONParser().parse(request)
        Serializer = BadgeSerializer(data=NewBadge)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET'])
def UserTrailCompletionList(request, pk):
    try:
        UserCompletedTrails = TrailCompletion.objects.filter(user=pk).filter(completion=True)
    except UserCompletedTrails.DoesNotExist:
        return JsonResponse({'message': 'This User has no completed trails'}, stastatus=status.HTTP_404_NOT_FOUNDtus)
        
    Serializer = TrailCompletionSerializer(UserCompletedTrails, many=True)
    return JsonResponse(Serializer.data, safe=False)


@api_view(['GET'])
def UserCompletionLengths(request, pk):
    
    
    UserCompletedTrails = TrailCompletion.objects.filter(user=pk).filter(completion=True)
    TrailData = Trail.objects.all()
    
    returnData = []
    for obj in UserCompletedTrails:
        trail_id = obj.trail_id.id
        length = TrailData.filter(pk=trail_id)[0].length
        returnData.append({
                      'date' : obj.date,
                      'length' : length,
                      })
        
    serialized_objects = UserTrailLengthSerializer(returnData, many=True)

    return JsonResponse(serialized_objects.data, safe=False)

    
