from django import forms
from django.forms import ModelForm
from .models import Resume, Address, Language, Education, Skills, Hobbies, References, History, ResumeTemp


class ResumeForm(forms.ModelForm):
    phone = forms.CharField()
    summary = forms.CharField(widget=forms.Textarea)
    month = forms.CharField()
    day = forms.CharField()
    year = forms.CharField()


    class Meta:
        model = Resume 
        fields = ( 
            'phone', 'summary','month','day','year'
            )

class ResumeT(forms.ModelForm):


    class Meta:
        model = ResumeTemp 
        fields = ( 
            'resume_template',
            )
    resume_template = forms.CharField(widget=forms.HiddenInput())


class ResumeAddress(forms.ModelForm):
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    zip_code = forms.CharField()


    class Meta:
        model = Address
        fields = ( 
            'address', 'city', 'country', 'zip_code'
            )


class ResumeLanguage(forms.ModelForm):
    name = forms.CharField()
    skill = forms.CharField()
    

    class Meta:
        model = Language
        fields = ( 
            'name', 'skill'
            )


class ResumeEducation(forms.ModelForm):
    name = forms.CharField()
    address = forms.CharField()
    degree = forms.CharField()
    status = forms.CharField()
    month = forms.CharField()
    day = forms.CharField()
    year = forms.CharField()


    class Meta:
        model = Education
        fields = ( 
            'name', 'address', 'degree', 'status', 'month', 'day', 'year'
            )


class ResumeSkills(forms.ModelForm):
    name = forms.CharField()
    skill = forms.CharField()
    

    class Meta:
        model = Skills
        fields = ( 
            'name', 'skill'
            )


class ResumeHobbies(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField()
    
    class Meta:
        model = Hobbies
        fields = ( 
            'name', 'description'
            )


class ResumeHistory(forms.ModelForm):
    title = forms.CharField()
    name = forms.CharField()
    address = forms.CharField()
    month_f = forms.CharField()
    year_f = forms.CharField()
    month_t = forms.CharField()
    year_t = forms.CharField()
    description = forms.CharField()
    

    class Meta:
        model = History
        fields = ( 
            'title', 'name', 'address', 'month_f', 'year_f', 'month_t', 'year_t', 'description'
            )


class ResumeReferences(forms.ModelForm):
    name = forms.CharField()
    phone = forms.CharField()
    title = forms.CharField()
    company_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = References
        fields = ( 
            'name', 'phone', 'title', 'company_name', 'email'
            )