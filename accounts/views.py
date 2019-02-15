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
		form = UserRegisterForm(self.request.POST)
		
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data.get('password'))
			user.save()
			account = Account(user_id=user.id)
			account.save()

			user = authenticate(
					username=form.cleaned_data.get('username'),
					password=form.cleaned_data.get('password')
			)
			messages.success(self.request, f'Account Created you may now Log in!')
			return redirect('/accounts/login')
		else:
			print(form.errors)

		return render(self.request, self.template_name, {'form': form})

	def get(self,*args,**kwargs): 
		form = UserRegisterForm()
		return render(self.request, self.template_name, {'form': form})

