from django.contrib import admin
from .models import *

admin.site.register(Trail)
admin.site.register(TrailComment)
admin.site.register(TrailLike)
admin.site.register(TrailMessage)
admin.site.register(TrailCompletion)
admin.site.register(Account)
admin.site.register(Badge)
admin.site.register(TrailMessageLike)
admin.site.register(Feedback)