from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("update_comments",views.update_comments,name = "update_comments")
    


]