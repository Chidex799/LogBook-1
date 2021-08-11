from django.contrib import admin
from .models import User, InstitutionSupervisor, UniversitySupervisor

# Register your models here.
admin.site.register(User)
admin.site.register(InstitutionSupervisor)
admin.site.register(UniversitySupervisor)