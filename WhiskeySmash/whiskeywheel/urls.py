from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('wheel', views.wheel, name='wheel'),
    path('wheelsend', views.wheelsend, name='wheelpost'),
    path('grid', views.grid, name='grid'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

]