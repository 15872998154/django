from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
    
    path('', v.blog_list,name = "blog_list"),
    path('detail/<int:blog_id>', v.blog_detail,name = "blog_detail"),
    path('cates/<int:type_id>',v.blogs_with_type,name = "blogs_with_type"),
    path('date/<int:year>/<int:month>',v.blogs_with_date,name = "blogs_with_date"),
    path('comment_login',v.comment_login,name = "comment_login"),


]