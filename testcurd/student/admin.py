from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class ArticleAdmin(admin.ModelAdmin):
    #展示字段
    list_display = ('id','stu_name','stu_age','score')
    #可修改字段
    fields = ('stu_name','stu_age','score')