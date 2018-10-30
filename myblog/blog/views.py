from django.shortcuts import render
from .models import Article
#from django.http import HttpResposneRedirect
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
	articles = Article.objects.all()

	return render(request,'blog/index.html',{'articles':articles})

def article(request,article_id):
	article = Article.objects.get(pk=article_id)
	article_dict = {'article':article}
	return render(request,'blog/article.html',article_dict)

def create_article(request):
	return render(request,'blog/create_article.html')

def create_article_action(request):
	title = request.POST['title']
	content = request.POST['content']
	Article.objects.create(title = title,content = content)
	#articles = Article.objects.all()
	return HttpResponseRedirect('/blog') 

def update(request,article_id):
	article = Article.objects.get(pk=article_id)
	return render(request,'blog/update.html',{'article':article})

def update_action(request):
	article_id = request.POST['article_id']
	title = request.POST['title']
	content = request.POST['content']
	
	article = Article.objects.get(pk=article_id)
	article.title = title
	article.content = content
	article.save()

	return HttpResponseRedirect('/blog/article/{}'.format(article.id)) 

	
