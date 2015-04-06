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

class OwnedTwit_Admin(admin.ModelAdmin):
    class Meta:
        model = OwnedTwit

admin.site.register(OwnedTwit, OwnedTwit_Admin)

class RTedTwit_Admin(admin.ModelAdmin):
    class Meta:
        model = RTedTwit

admin.site.register(RTedTwit, RTedTwit_Admin)

class Twits_Admin(admin.ModelAdmin):
    class Meta:
        model = Twits

admin.site.register(Twits, Twits_Admin)