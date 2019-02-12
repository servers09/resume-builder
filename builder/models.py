from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    resume_template = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    month = models.CharField(max_length=20)
    day = models.CharField(max_length=15)
    year = models.CharField(max_length=15)
    address = models.ManyToManyField('builder.Address',blank=True)
    language = models.ManyToManyField('builder.Language',blank=True)
    education = models.ManyToManyField('builder.Education',blank=True)
    skills = models.ManyToManyField('builder.Skills',blank=True)
    hobbies = models.ManyToManyField('builder.Hobbies',blank=True)
    history = models.ManyToManyField('builder.History',blank=True)
    references = models.ManyToManyField('builder.References',blank=True)
    summary = models.TextField(max_length=500)


class Address(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=80) 
    country = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=10)

class Language(models.Model):
    name = models.CharField(max_length=80)
    skill = models.CharField(max_length=50)

class Education(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    degree = models.CharField(max_length=80)
    status = models.CharField(max_length=80)
    month = models.CharField(max_length=80)
    day = models.CharField(max_length=80)
    year = models.CharField(max_length=80)

class Skills(models.Model):
    name = models.CharField(max_length=80)
    skill = models.CharField(max_length=80)

class Hobbies(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    month_f = models.CharField(max_length=80)
    year_f = models.CharField(max_length=80)
    month_t = models.CharField(max_length=80)
    year_t = models.CharField(max_length=80)
    description = models.CharField(max_length=100)

class References(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    company_name = models.CharField(max_length=80)
    email = models.EmailField()
