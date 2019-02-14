from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username','email','password1','password2',)

	def clean_email(self):
		email = User.objects.filter(email=self.cleaned_data['email'])
		if email.exists():
			raise forms.ValidationError('Email already exists!')
		return self.cleaned_data['email']

	def clean_username(self):
		username = User.objects.filter(username=self.cleaned_data['username'])
		if username.exists():
			raise forms.ValidationError('Username already exists!')
		return self.cleaned_data['username']

	def clean(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 != password2:
			raise forms.ValidationError('Passwords did not match!')
			return self.cleaned_data


class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.TextInput(attrs={'type':'password'}))

	class Meta:
		model = User
		fields = ('username','password',)

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']

		user = authenticate(username=username,password=password)

		if user is not None:
			return self.cleaned_data
		raise forms.ValidationError('Invalid Username or Password')
