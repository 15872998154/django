from django.contrib import admin
from .models import HeroType,Hero
# Register your models here.
@admin.register(HeroType)
class HeroTypeAdmin(admin.ModelAdmin):
    list_display = ('heroTypeId','hero_type')
    list_display_links = ('heroTypeId','hero_type')

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ('hero_id','hero_name','heroType','hero_word','hero_photo')
    #对数据进行过滤所要依据的字段
    list_filter =('heroType',) #过滤器
    #定义可以修改的字段
    list_display_links = ('hero_name','heroType','hero_word','hero_photo',)

admin.site.site_header = "王者荣耀" 
admin.site.site_title = "王者荣耀"