"""FaceRecognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('home.urls')),
     path('getstarted', include('home.urls')),
     path('signin', include('home.urls')),
     path('attendance', include('home.urls')),
     path('crime', include('home.urls')),
     path('logoutUser', include('home.urls')),
     path('camera', include('home.urls')),
     path('cameracrime', include('home.urls')),
     path('comingsoon', include('home.urls')),
     path('signuphelper', include('home.urls')),
     path('cameraout', include('home.urls')),

     

]
