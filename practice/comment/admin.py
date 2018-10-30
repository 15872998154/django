from django.contrib import admin
from .models import Comment
# Register your models here.
@admin.register(Comment)
class ConmmentAdmin(admin.ModelAdmin):
    list_display = ('content_object','text','comment_time','user')