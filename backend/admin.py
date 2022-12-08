from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Trail)
admin.site.register(TrailComment)
admin.site.register(TrailLike)
admin.site.register(TrailCompletion)
admin.site.register(Account)
