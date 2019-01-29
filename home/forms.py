from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget = forms.TextInput(attrs={'type':'password'}))
	class Meta:
		model = User
		fields = ('username','email','password','first_name','last_name')