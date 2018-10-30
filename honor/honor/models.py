from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Hero(models.Model):
    #主键 英雄id
    hero_id = models.IntegerField(primary_key = True,verbose_name = "编号")
    #英雄名属性
    hero_name = models.CharField(max_length = 48,verbose_name = "英雄名称")
    #英雄所属类型如射手 外键 
    heroType = models.ForeignKey('HeroType',on_delete = models.CASCADE,verbose_name = "英雄定位")
    #英雄描述信息
    hero_word = models.CharField(max_length = 512,verbose_name = "人物台词")
    #英雄攻略
    hero_gonglue = RichTextField(default = "",verbose_name = "英雄攻略")
    #英雄技能描述
    hero_skill = RichTextField(default = "",verbose_name = "英雄技能")
    #hero图片地址
    hero_photo = models.CharField(max_length = 48,verbose_name = "资源地址")
    #后台界面显示 王者荣耀英雄
    class Meta:
        verbose_name_plural = '王者荣耀英雄'
    def __str__(self):
        return self.hero_name

class HeroType(models.Model):
    #主键 英雄类型编号
    heroTypeId = models.IntegerField(primary_key = True,verbose_name = "编号")
    #英雄类别
    hero_type = models.CharField(max_length = 32,verbose_name = "英雄定位")
    #后台界面显示 王者荣耀英雄类别
    class Meta:
        verbose_name_plural = '王者荣耀英雄类别'
    def __str__(self):
        return self.hero_type


