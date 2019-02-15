from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
	"""
	Register Validation
	"""
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Username')}),max_length=255)
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':('Email Address')}),required=True)
	password = forms.CharField(widget = forms.TextInput(attrs={'placeholder':('Password'),'type':'password'}),max_length = 50,min_length=6)
	confirm = forms.CharField(widget = forms.TextInput(attrs={'placeholder':('Confirm Password'),'type':'password'}),max_length = 50,min_length=6)
	

	class Meta:
		model = User
		fields = ('username','email','password','confirm',)

	def clean_email(self):
		email = User.objects.filter(email=self.cleaned_data['email'])
		if email.exists():
			raise forms.ValidationError('Email already existed!')
		return self.cleaned_data['email']

	def clean_username(self):
		username = User.objects.filter(username=self.cleaned_data['username'])
		if username.exists():
			raise forms.ValidationError('Username already exists!')
		return self.cleaned_data['username']

	def clean(self):
		password = self.cleaned_data.get('password')
		confirm = self.cleaned_data.get('confirm')

		if password != confirm:
			raise forms.ValidationError('Passwords did not match!')
		return self.cleaned_data



