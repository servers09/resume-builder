from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import calendar, datetime

class Resume(models.Model):
    """
    Resume
    
    """

    MONTH = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    DAY = []
    for y in range(1, (31+1)):
        DAY.append((y,y))
    YEAR = []
    for z in range(1900, (datetime.datetime.now().year+1)):
        YEAR.append((z,z))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    phone = models.CharField(max_length=15)
    month = models.CharField(max_length=20,choices=MONTH)
    day = models.CharField(max_length=15,choices=DAY)
    year = models.CharField(max_length=15,choices=YEAR)
    address = models.ManyToManyField('builder.Address',blank=True)
    language = models.ManyToManyField('builder.Language',blank=True)
    education = models.ManyToManyField('builder.Education',blank=True)
    skills = models.ManyToManyField('builder.Skills',blank=True)
    hobbies = models.ManyToManyField('builder.Hobbies',blank=True)
    history = models.ManyToManyField('builder.History',blank=True)
    references = models.ManyToManyField('builder.References',blank=True)
    summary = models.TextField(max_length=500)


class ResumeTemp(models.Model):
    """
    ResumeTemp
    
    """
    resume_template = models.CharField(max_length=2)


class Address(models.Model):
    """
    Address
    
    """

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=80) 
    country = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=10)

class Language(models.Model):
    name = models.CharField(max_length=80)
    skill = models.CharField(max_length=50)

class Education(models.Model):
    """
    Education
    
    """

    MONTH = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    DAY = []
    for y in range(1, (31+1)):
        DAY.append((y,y))
    YEAR = []
    for z in range(1900, (datetime.datetime.now().year+1)):
        YEAR.append((z,z))
    STATUS = (('', 'Status'),('graduated', 'Graduated'),('graduating', 'Graduating'),('enrolled', 'Currently Enrolled'))

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    degree = models.CharField(max_length=80)
    status = models.CharField(max_length=80,choices=STATUS)
    month = models.CharField(max_length=20,choices=MONTH)
    day = models.CharField(max_length=15,choices=DAY)
    year = models.CharField(max_length=15,choices=YEAR)

class Skills(models.Model):
    """
    Skills
    
    """

    name = models.CharField(max_length=80)
    skill = models.CharField(max_length=80)

class Hobbies(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)

class History(models.Model):
    """
    History
    
    """

    MONTH = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    YEAR = []
    for z in range(1900, (datetime.datetime.now().year+1)):
        YEAR.append((z,z))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    month_f = models.CharField(max_length=80,choices=MONTH)
    year_f = models.CharField(max_length=80,choices=YEAR)
    month_t = models.CharField(max_length=80,choices=MONTH)
    year_t = models.CharField(max_length=80,choices=YEAR)
    description = models.CharField(max_length=100)

class References(models.Model):
    """
    References
    
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    company_name = models.CharField(max_length=80)
    email = models.EmailField()
