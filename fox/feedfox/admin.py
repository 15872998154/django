from django.contrib import admin

# Register your models here.
from .models import Article,Novel,NovelType



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #展示字段
    list_display = ('id','title','belong_novel',)
    #可修改字段
    fields = ('title','content','belong_novel')

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    #展示字段
    list_display = ('id','novel_name','get_novel_type','description','image')

    list_display_links = ('id','novel_name','get_novel_type','description','image')
    #可修改字段
    fields = ('novel_name','novel_type','description','image')

@admin.register(NovelType)
class NovelTypeAdmin(admin.ModelAdmin):
    #展示字段
    list_display = ('id','type_name',)
    #可修改字段
    fields = ('type_name',)