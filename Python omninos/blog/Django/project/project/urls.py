"""project URL Configuration

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
import imp
from django.contrib import admin
from django.urls import path
from flygo_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("list",views.list,name="list"),
    path("<int:id>",views.Booking,name="edit"),
    path("d<int:id>",views.data_delete,name="del"),
    path("booking",views.Booking,name="booking"),
    path("login",views.login,name="login"),
    path("register",views.registration,name="register"),
    path('logout',views.logout,name='logout'),
]
