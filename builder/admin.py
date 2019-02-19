from django.contrib import admin
from .models import Resume, Address, Language, Education, Skills, Hobbies, References,ResumeTemp

admin.site.register(Resume)
admin.site.register(Address)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Hobbies)
admin.site.register(References)
admin.site.register(ResumeTemp)