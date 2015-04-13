#-*-coding:utf-8-*-
from django.http import *
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext, redirect
from .models import *
from .forms import *
from datetime import *
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf

def home(request):
	return render(request, 'base.html', {})


def profile(request, user):
	owner_user = get_object_or_404(User, username = user)
	user2 = request.user
	f = Follower_Following.objects.get_or_create(user=owner_user)
	follow = Follower_Following.objects.get(user=owner_user)
	tweets = Twits.objects.filter(user = owner_user).order_by('-timestamp')
	

	user = request.user
	return render(request, 'own.html', {'tweets':tweets,'owner_user':owner_user,'follow':follow,'user':user,'user2':user2})

def search(request, q):
	twits = Twit.objects.filter(content__istartswith=q)
	if len(twits) is 0:
		return HttpResponse (u'404')
	else:
		return render(request, 'search.html', {'twits':twits,})
		
def posttwit(request):
	twit_form = AddTwitForm(request.POST or None)

	if twit_form.is_valid():
		new_twit = twit_form.save(commit=False)
		new_twit.user = request.user
		new_twit.mainuser = request.user
		new_twit.rt_count = 0
		new_twit.fav_count = 0
		new_twit.save()
		#twitt = Twit.objects.get(id=new_twit.id)
		owned = OwnedTwit.objects.create(user=request.user, twit=new_twit, timestamp=new_twit.timestamp)
		g_owned = Twits.objects.create(user=request.user, twit_type=owned, twit_type_id=owned.id)
		g_owned.save()

		return HttpResponse (u'added')


def follow(request, f_id, f_id2):
	a_user = User.objects.get(id=f_id)
	b_user = User.objects.get(id=f_id2)
	a, c = Follower_Following.objects.get_or_create(user=a_user)
	b, c = Follower_Following.objects.get_or_create(user=b_user)
	a.following.add(b_user)
	b.followers.add(a_user)

	return HttpResponse (u'oldu')

def unfollow(request, f_id, f_id2):
	a_user = User.objects.get(id=f_id)
	b_user = User.objects.get(id=f_id2)
	a = Follower_Following.objects.get(user=a_user)
	b = Follower_Following.objects.get(user=b_user)
	a.following.remove(b_user)
	b.followers.remove(a_user)

	return HttpResponse (u'oldu')

def retweet(request, t_id):
	user = request.user
	twit = Twit.objects.get(id=t_id)
	rted = RTedTwit.objects.create(user=user, twit=twit, timestamp=twit.timestamp)
	g_rted = Twits.objects.create(user=request.user, twit_type=rted, twit_type_id=rted.id)
	g_rted.save()

	return HttpResponse (u'oldu')

def fav(request, twit_id):
	user = request.user
	twit = Twit.objects.get(id=twit_id)
	a, c = Fav.objects.get_or_create(user=user)
	a.faved_twits.add(twit)

	return HttpResponse (u'oldu')

def favedtwits(request, user):
	owner_user = get_object_or_404(User, username = user)
	faved, c = Fav.objects.get_or_create(user=owner_user)


	return render(request, 'faved.html', {'faved':faved,})
