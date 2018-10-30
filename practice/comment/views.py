
from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog
from django.urls import reverse
# Create your views here.
def update_comments(request):
    user = request.user
    text = request.POST.get('text','错误')
    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id','31'))
    print("*"*50)
    content_type = ContentType.objects.get(model = 'blog')
    
    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_type = content_type
    # ContentType.object.filter(model = )
    comment.object_id = object_id
    comment.save()
    print("*"*100)
    previous_page = request.META.get('HTTP_REFERER',reverse('home'))
    return redirect(previous_page)

def comment_list(request,blog_pk):
    context = {}
    content_type = ContentType.objects.get(model = 'blog')
    context['comments'] = Comment.objects.filter(content_type = content_type,object_id = blog_pk)
