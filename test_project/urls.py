"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


import sys
sys.path.append("..")




from django.contrib import admin
from django.urls import path

from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("login", views.LogIn.as_view(), name="login"),
    path("logout", views.LogOut.as_view(), name="logout"),
    path("signup", views.SignUp.as_view(), name="signup"),
    path("course/<int:course_number>", views.CourseView.as_view()),
    path("course/<int:course_number>/rate", views.RateView.as_view()),
    path("course/<int:course_number>/rate", views.RateView.as_view()),
]
