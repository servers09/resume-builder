from django import forms
import datetime
from django.forms import ModelForm
from .models import Resume, Address, Language, Education, Skills, Hobbies, References, History


STATUS = (
    ('', 'Status'),
    ('graduated', 'Graduated'),
    ('graduating', 'Graduating'),
    ('enrolled', 'Currently Enrolled')
    )

MONTH = (
    ('', 'Month'),
    ('JAN', 'January'),
    ('FEB', 'Febuary'),
    ('MAR', 'March'),
    ('APR', 'April'),
    ('MAY', 'May'),
    ('JUN', 'June'), 
    ('JUL', 'July'),
    ('AUG', 'August'),
    ('SEP', 'September'),
    ('OCT', 'October'),
    ('NOV', 'November'),
    ('DEC', 'December')
    )

DAY = []

for y in range(1, (31+1)):
    DAY.append((y,y))

YEAR = []

for z in range(1900, (datetime.datetime.now().year+1)):
    YEAR.append((z,z))



class ResumeForm(forms.ModelForm):
    phone = forms.CharField(widget = forms.TextInput())
    summary = forms.CharField(widget=forms.Textarea)
    month = forms.CharField(widget = forms.TextInput())
    day = forms.CharField(widget = forms.TextInput())
    year = forms.CharField(widget = forms.TextInput())
    class Meta:
        model = Resume 
        fields = ( 
            'phone', 'summary','month','day','year'
            )

class ResumeAddress(forms.ModelForm):
    address = forms.CharField(widget = forms.TextInput())
    city = forms.CharField(widget = forms.TextInput())
    country = forms.CharField(widget = forms.TextInput())
    zip_code = forms.CharField(widget = forms.TextInput())
    class Meta:
        model = Address
        fields = ( 
            'address', 'city', 'country', 'zip_code'
            )

class ResumeLanguage(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    skill = forms.CharField(widget = forms.TextInput())
    
    class Meta:
        model = Language
        fields = ( 
            'name', 'skill'
            )

class ResumeEducation(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    address = forms.CharField(widget = forms.TextInput())
    degree = forms.CharField(widget = forms.TextInput())
    status = forms.CharField(widget = forms.TextInput())
    month = forms.CharField(widget = forms.TextInput())
    day = forms.CharField(widget = forms.TextInput())
    year = forms.CharField(widget = forms.TextInput())

    class Meta:
        model = Education
        fields = ( 
            'name', 'address', 'degree', 'status', 'month', 'day', 'year'
            )

class ResumeSkills(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    skill = forms.CharField(widget = forms.TextInput())
    
    class Meta:
        model = Skills
        fields = ( 
            'name', 'skill'
            )

class ResumeHobbies(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    description = forms.CharField(widget = forms.TextInput())
    
    class Meta:
        model = Hobbies
        fields = ( 
            'name', 'description'
            )

class ResumeHistory(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput())
    name = forms.CharField(widget = forms.TextInput())
    address = forms.CharField(widget = forms.TextInput())
    month_f = forms.CharField(widget = forms.TextInput())
    year_f = forms.CharField(widget = forms.TextInput())
    month_t = forms.CharField(widget = forms.TextInput())
    year_t = forms.CharField(widget = forms.TextInput())
    description = forms.CharField(widget = forms.TextInput())
    
    class Meta:
        model = History
        fields = ( 
            'title', 'name', 'address', 'month_f', 'year_f', 'month_t', 'year_t', 'description'
            )
class ResumeReferences(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput())
    phone = forms.CharField(widget = forms.TextInput())
    title = forms.CharField(widget = forms.TextInput())
    company_name = forms.CharField(widget = forms.TextInput())
    email = forms.EmailField()