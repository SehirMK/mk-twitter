from django.contrib import admin

from .models import *

class TwitAdmin(admin.ModelAdmin):
    class Meta:
        model = Twit

admin.site.register(Twit, TwitAdmin)