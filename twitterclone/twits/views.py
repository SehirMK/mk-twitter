#-*-coding:utf-8-*-
from django.http import *
from .models import *
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf



# Create your views here.
def profile(request, user):
	owner_user = get_object_or_404(User, username = user)
	tweets = Twit.objects.filter(user = owner_user).order_by('-timestamp')
	return render(request, 'own.html', {'tweets':tweets,})

@csrf_exempt
def gonder(request):
	if request.method == 'POST':
		twittertext = request.POST.get('tweet')
		retweetcount = request.POST.get('rt')
		favcount = request.POST.get('fav')
		register_tweet = tweet(tweet_text=twittertext, rt_counts = retweetcount, fav_counts = favcount)
		register_tweet.save()
		return HttpResponse (u'Tweet başarıyla gönderildi: %s '% twittertext)
	else:
		return HttpResponse(u'404')



