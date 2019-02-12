from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ResumeForm ,ResumeAddress, ResumeLanguage, ResumeEducation, ResumeSkills, ResumeHobbies , ResumeHistory, ResumeReferences
from .models import Resume, Address, Language, Education, Skills, Hobbies, References, History
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .utils import render_to_pdf
from django.http import HttpResponse

class ResumeEdit(TemplateView):
    template_name = 'builder/edit.html'
    def post(self,*args,**kwargs):
        form_main = ResumeForm(self.request.POST)
        if form_main.is_valid():
            file = Resume()
            file.phone = form.cleaned_data['phone']
            file.summary = form.cleaned_data['summary']
            file.month = form.cleaned_data['month']
            file.day = form.cleaned_data['day']
            file.year = form.cleaned_data['year']
            file  = form.save(commit=False)
            file.user = self.request.user
            file.save()
            return redirect('/builder/preview/'+str(kwargs.get('id'))+'/')

    def get(self,*args,**kwargs):
        user_data = User.objects.get(id=self.request.user.id)
        form = ResumeForm()
        return render(self.request, self.template_name, {'form': form,'user_data':user_data,})



class Choose(TemplateView):
	def get(self,*args,**kwargs):
		return render(self.request,'builder/choose.html')

class GeneratePdf(TemplateView):

    def get(self, request, *args, **kwargs):
        data = Resume.objects.get(id=kwargs.get('id'))
        
        table = {
        'resume_form' : data,
                }   
        if resume_template == '1':
             pdf = render_to_pdf('builder/templates/resume-templates/traditional.html', table)
        elif resume_template == '2':
            pdf = render_to_pdf('builder/templates/resume-templates/improved.html', table)
        elif resume_template == '3':
            pdf = render_to_pdf('builder/templates/resume-templates/blue-tabs.html', table)

        return HttpResponse(pdf, content_type='application/pdf')