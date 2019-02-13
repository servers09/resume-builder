from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import LoginForm ,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout

class UserLogin(TemplateView):
	template_name = 'accounts/login.html'
	def post(self,*args,**kwargs):
		forms = LoginForm(self.request.POST)
		if forms.is_valid():
			user = authenticate(username=forms.cleaned_data.get('username')
        		,password=forms.cleaned_data.get('password'))
			login(self.request,user)
			return redirect('/builder/edit/'+str(self.request.user.id)+'/')

	def get(self,*args,**kwargs):
		forms = LoginForm()
		return render(self.request, self.template_name, {'forms': forms,})


