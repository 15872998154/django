from django.db import models

# Create your models here.

class Article(models.Model): #小说具体内容
    
    title = models.CharField(max_length = 60,default="",verbose_name = "标题")
    content = models.TextField(default="",verbose_name = "内容")
    belong_novel = models.ForeignKey('Novel',on_delete = models.CASCADE,verbose_name = "小说名",default=1)

    class Meta:
        verbose_name_plural = '小说章节管理'


class Novel(models.Model): #小说信息
    author = models.CharField(max_length=60,default="")
    novel_type  = models.ForeignKey("NovelType",on_delete = models.DO_NOTHING,default=1,verbose_name = "小说类型",)
    novel_name = models.CharField(max_length = 60,verbose_name = "小说名",)
    description = models.CharField(max_length = 1000,default="",verbose_name = "描述",)
    def get_all_article(self):
        print("zz")
        return self.article_set.all()
    
    def get_novel_type(self):
        return self.novel_type.type_name
    
    class Meta:
        verbose_name_plural = '小说管理'

    def __str__(self):
        return self.novel_name


class NovelType(models.Model): #小说分类
    type_name = models.CharField(max_length = 32,verbose_name = "小说分类",)
    
    def __str__(self):
        return self.type_name 
    class Meta:
        verbose_name_plural = '小说分类'

