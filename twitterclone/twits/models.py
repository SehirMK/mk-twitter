from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Twit(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	content = models.TextField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	fav_count = models.IntegerField(default=0, null=True, blank=True)
	rt_count = models.IntegerField(default=0, null=True, blank=True)
	rt_users = models.ManyToManyField(User, related_name='rt_users', null=True, blank=True)
	fav_users = models.ManyToManyField(User, related_name='fav_users', null=True, blank=True)
	def __unicode__(self):
		return self.content

class Follower_Following(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	followers = models.ManyToManyField(User, null=True, blank=True, related_name='followers')
	following = models.ManyToManyField(User, null=True, blank=True, related_name='following')
