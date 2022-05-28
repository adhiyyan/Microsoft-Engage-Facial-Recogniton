from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
     path("", views.index, name='home'),
     path("getstarted", views.getstarted, name='getstarted'),
     path("signin", views.signin, name='signin'),
     path("attendance", views.attendance, name='attendance'),
     path("crime", views.crime, name='crime'),
     path("logoutUser", views.logoutUser, name='logoutUser'),
     path("camera", views.camera, name='camera'),
     path("cameracrime", views.cameracrime, name='cameracrime'),
     path("comingsoon", views.comingsoon, name='comingsoon'),
     path("signuphelper", views.signuphelper, name='signuphelper'),
     path("cameraout", views.cameraout, name='cameraout'),

]
urlpatterns+=staticfiles_urlpatterns()