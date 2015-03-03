from django.contrib import admin

from .models import *

class TwitAdmin(admin.ModelAdmin):
    class Meta:
        model = Twit

admin.site.register(Twit, TwitAdmin)

class Follower_FollowingAdmin(admin.ModelAdmin):
    class Meta:
        model = Follower_Following

admin.site.register(Follower_Following, Follower_FollowingAdmin)