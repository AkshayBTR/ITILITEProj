from django import forms
from django.contrib.auth.models import User
from app.models import *


class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=100,min_length=8,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('gender','work_type','skills','profile_pic')
