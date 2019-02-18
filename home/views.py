from django.shortcuts import render

from django.views.generic import TemplateView

class Home(TemplateView):
	def get(self,*args,**kwargs):
		 return render(self.request,'home/home2.html')