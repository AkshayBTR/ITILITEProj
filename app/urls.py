from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('hai/<name>',views.hainame,name="hai"),
    path('add/<a>/<b>',views.add,name="add"),
    path('temp/',views.tempdemo,name="tempdemo"),
    path('grt/<a>/<b>',views.grt2,name="grt2"),
    path('homepage/',views.hometemp,name="hometemp"),
    path('aboutus/',views.abouttemp,name="aboutus"),
    path('register/',views.register,name="register"),
    # path("profile/<id>",views.show_data,name="profile"),
]
