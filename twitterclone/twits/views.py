#-*-coding:utf-8-*-
from django.http import *
from .models import *
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404



# Create your views here.
def profile(request, user):
	owner_user = get_object_or_404(User, username = user);
	tweets = Twit.objects.filter(user = owner_user).order_by('-timestamp')
	return render(request, 'own.html', {'tweets':tweets,})


