#-*-coding:utf-8-*-
from django.http import *
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext, redirect
from .models import *
from .forms import *
from datetime import *
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf


def profile(request, user):
	owner_user = get_object_or_404(User, username = user)
	tweets = Twit.objects.filter(user = owner_user).order_by('-timestamp')
	return render(request, 'own.html', {'tweets':tweets,})

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
		new_twit.rt_count = 0
		new_twit.fav_count = 0
		new_twit.save()

		return HttpResponse (u'added')




