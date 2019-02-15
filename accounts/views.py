from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import UserRegisterForm , LoginForm
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
		form = UserRegisterForm(self.request.POST)
		
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data.get('password'))
			user.save()

			user = authenticate(
					username=form.cleaned_data.get('username'),
					password=form.cleaned_data.get('password')
			)
			messages.success(self.request, f'Account Created you may now Log in!')
			return redirect(reverse('accounts:login'))

		return render(self.request, self.template_name, {'form': form})

	def get(self,*args,**kwargs): 
		form = UserRegisterForm()
		return render(self.request, self.template_name, {'form': form})


class UserLogin(TemplateView):
	"""
	Login View
	GET - get forms and render template
	POST - login user
	"""
	template_name = 'accounts/login.html'

	def post(self,*args,**kwargs):
		form = LoginForm(self.request.POST)

		if form.is_valid():
			user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
			login(self.request,user)
			return redirect(reverse('accounts:login'))

		return render(self.request, self.template_name, {'form': form})

	def get(self,*args,**kwargs):
		form = LoginForm()
		return render(self.request, self.template_name, {'form': form})