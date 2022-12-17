"""hikeable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/trails', views.TrailList, name='trail_list'),
    path('api/trails/<int:pk>', views.TrailDetail, name='trail_detail'),
    path('api/trails/comments', views.TrailCommentList, name='trailcomment_list'),
    path('api/trails/<int:pk>/comments',
         views.TrailCommentDetail, name='trailcomment_detail'),
    path('api/trails/likes', views.TrailLikeList, name='traillike_list'),
    path('api/trails/<int:pk>/likes', views.TrailLikeGet, name='traillike_get'),
    path('api/trails/likes/<int:pk>', views.TrailLikePut, name='traillike_put'),
    path('api/trails/completions', views.TrailCompletionList,
         name='trailcompletion_list'),
    path('api/trails/<int:pk>/completions',
         views.TrailCompletionGet, name='trailcompletion_get'),
    path('api/trails/completions/<int:pk>',
         views.TrailCompletionPut, name='trailcompletion_put'),
    path('api/users', views.register, name='account_post'),
    path('api/users/<str:uid>', views.get, name='account_get'),
    path('api/users/<str:uid>', views.get, name='account_get'),
    path('api/users/<int:pk>/badges', views.UserBadgeList, name='user_badges'),
    path('api/users/<int:pk>/completions', views.UserTrailCompletionList, name='user_completion_trails'),
    path('api/users/<int:pk>/completion-lengths', views.UserCompletionLengths, name='user_completion_lengths'),
    path('api/users/<int:pk>/messages', views.UserMessages, name='user_messages'),
    path('api/users/<int:pk>/trail-comments', views.UserTrailComments, name='user_trail_comments'),
    
    path('api/trails/messages', views.TrailMessageList, name='trailmessage_list'),
    path('api/trails/<int:pk>/messages', views.TrialMessageGet, name='trailmessage_get'),
    path('api/trails/messages/<int:pk>', views.TrailMessagePut, name='trailmessage_put')
]
