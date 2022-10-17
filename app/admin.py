from django.contrib import admin
from app import models
from django_reverse_admin import ReverseModelAdmin
from django.contrib.auth.models import User
# Register your models here.

class ProfileInline(ReverseModelAdmin):
    inline_reverse=['user',]
    inline_type='stacked'

admin.site.register(models.Skills)
admin.site.register(models.Profile,ProfileInline)