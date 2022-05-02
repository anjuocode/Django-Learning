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
from django.contrib import admin
from django.urls import path
from project_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("form",views.registration,name="form"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("",views.home,name="home"),
    path("rafting",views.rafting,name="rafting"),
    path("parag",views.parag,name="parag"),
    path("trek",views.treking,name="trek"),
    path("navbar",views.navbar,name="navbar")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)