from distutils.command.upload import upload
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skills(models.Model):
    skillname=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.skillname
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10,choices=(("Male","Male"),("Female","Female"),("Other","Other")))
    work_type=models.CharField(max_length=30,choices=(("part_time","part_time"),("Full_time","Full_time")))
    skills=models.ManyToManyField(Skills,related_name="profiles")
    profile_pic=models.ImageField(upload_to="profile_pic")

    def __str__(self) -> str:
        return self.user.first_name



