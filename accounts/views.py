from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
from django.urls import reverse


class UserRegister(TemplateView):
	"""
	Register View
	GET - get forms and render template
	POST - register user account
	"""
	template_name = 'accounts/register.html'

	def post(self,*args,**kwargs):
		forms = UserRegisterForm(self.request.POST)
		
		if forms.is_valid():
			user = forms.save()
			user.set_password(forms.cleaned_data.get('password'))
			user.save()

			user = authenticate(
					username=forms.cleaned_data.get('username'),
					password=forms.cleaned_data.get('password')
					)
			messages.success(self.request, f'Account Created you may now Log in!')
			return redirect('/accounts/login')
		else:
			print(forms.errors)

		return render(self.request, self.template_name, {'forms': forms})

	def get(self,*args,**kwargs): 
		forms = UserRegisterForm()
		return render(self.request, self.template_name, {'forms': forms})

