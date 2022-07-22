from django.urls import path
from django.contrib import admin
from . import views
#http://127.0.0.1:8000/

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="home"),
    path("blogs", views.blogs, name="blogs"),
    
]