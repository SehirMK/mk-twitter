from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Twit(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, related_name='user')
	mainuser = models.ForeignKey(User, null=True, blank=True, related_name='mainuser')
	content = models.TextField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	timestamp2 = models.DateTimeField(auto_now_add=True, auto_now=False)
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


class RTedTwit(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	twit = models.ForeignKey(Twit, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	

class OwnedTwit(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	twit = models.ForeignKey(Twit, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
class Twits(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	twit_type_name = models.ForeignKey(ContentType)
	twit_type_id = models.PositiveIntegerField()
	twit_type = generic.GenericForeignKey('twit_type_name', 'twit_type_id')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

class Fav(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	faved_twits = models.ManyToManyField(Twit, null=True, blank=True)
	