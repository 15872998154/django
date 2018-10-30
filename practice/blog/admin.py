from django.contrib import admin
from .models import Blog,BlogType,ReadNum
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','getCount','blog_type','author','created_time']

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id','blog_type']

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['blog','count']  