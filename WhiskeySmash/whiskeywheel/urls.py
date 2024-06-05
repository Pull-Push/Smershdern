from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns =[
    path('', views.home),
    path('wheel', views.wheel),
    path('wheelsend', views.wheelsend)
]