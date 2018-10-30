from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BlogType(models.Model):
    blog_type = models.CharField(max_length = 20)
    def __str__(self):
        return self.blog_type
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'
    def getCount(self):
        return self.blog_set.count()

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add = True)
    last_update_time = models.DateTimeField(auto_now = True)
    blog_type = models.ForeignKey(BlogType,on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.title
    def getCount(self):
        return self.readnum.count

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'

class ReadNum(models.Model):
    count = models.IntegerField()
    blog = models.OneToOneField(Blog,on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.blog.title
    class Meta:
        #ordering = ['-created_time']
        verbose_name = '博客统计'
        verbose_name_plural = '博客统计'

