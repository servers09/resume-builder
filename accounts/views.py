from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import LoginForm ,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout


class UserRegister(TemplateView):
	template_name = 'accounts/register.html'
	def post(self,*args,**kwargs):
		form = UserRegisterForm(self.request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(self.request, f'Account created for {username}!')
			return redirect('/accounts/login')
		return render(self.request, self.template_name, {'form': form})
	def get(self,*args,**kwargs): 
		form = UserRegisterForm()
		return render(self.request, self.template_name, {'form': form})