from django.urls import path
from .import views
urlpatterns = [
path('',views.home,name='home'),
path('family',views.family,name='family'),
path('culture',views.culture,name='culture'),
path('charity',views.charity,name='charity'),
path('business',views.business,name='business'),
path("login",views.login,name="login"),
path("register",views.registration,name="register"),
path('logout',views.logout,name='logout'),
path('book',views.book,name="book"),
path('usercart',views.user_cart,name='usercart'),
path('base',views.base,name="base"),
path('contact',views.contact_us,name='contact'),

]


