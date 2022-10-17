from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to the project</h1>')

def home(request):
    return HttpResponse('<h1>welcome to homepage</h1>')

def hainame(request,name):
    return HttpResponse('<h2>Hello {}</h2>'.format(name))

def add(request,a,b):
    return HttpResponse("<h1>The sum of {} & {} is {}</h1>".format(a,b,int(a)+int(b)))
    

def tempdemo(request):
    fruits=['apple','banana','chikku','mango','dragon friut']
    return render(request,"template1.html",
    context={'name':"akshay",'Profession':"Data Scientist",'fruits':fruits})

def grt2(request,a,b):
    return render(request,"template2.html",context={'a':int(a),'b':int(b)})


def hometemp(request):
    return render(request,"Pages/home.html")

def abouttemp(request):
    return render(request,"Pages/about.html")

from django.core.files.storage import FileSystemStorage
from app.models import *
from django.contrib.auth.models import User
from app.forms import UserForm,ProfileForm

def register(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        profile=ProfileForm(request.POST,request.FILES)
        if user.is_valid() and profile.is_valid():
            password=user.cleaned_data["password"]
            user=user.save(commit=False)
            user.set_password(password)
            user.save()
            profile=profile.save(commit=False)
            profile.user=user
            profile.save()
            
        # first_name=request.POST.get("first_name")
        # last_name=request.POST.get("last_name")
        # username=request.POST.get("username")
        # email=request.POST.get("email")
        # password=request.POST.get("pwd")
        # gender=request.POST.get("gender")
        # worktype=request.POST.get("worktype")
        # skills=request.POST.getlist("skills")
        # if request.FILES:
        #     file=request.FILES['profilepic']
        # user=User(username=username,email=email,first_name=first_name,last_name=last_name)
        # user.set_password(password)
        # user.save()
        # user_profile=Profile.objects.get_or_create(user=user,gender=gender,work_type=worktype,profile_pic=file)[0]

        # #user=Profile.objects.get_or_create(name=name,email=email,gender=gender,profile_pic=file)[0]
        # for i in skills:
        #     sk=Skills.objects.get(skillname=i)
        #     user_profile.skills.add(sk)
        # user_profile.save()
        
        return HttpResponse("<h1>Form Submitted Successfully</h1>")
    userform=UserForm()
    profileform=ProfileForm()
    return render(request,"Pages/register.html",context={"userform":userform,"profileform":profileform})


# def show_data(request,id):
#     data=Register.objects.all()
#     return render(request,"Pages/profile.html",{"datas":data})

