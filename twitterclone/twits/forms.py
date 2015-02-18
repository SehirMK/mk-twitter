# -*- coding: utf-8 -*-
from .models import *
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class AddTwitForm(ModelForm):
	class Meta:
		model = Twit
        fields = ('content')
