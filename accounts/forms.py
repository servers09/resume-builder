from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.TextInput(attrs={'type':'password'}))