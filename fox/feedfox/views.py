from django.shortcuts import render,HttpResponse
from .models import Article,Novel,NovelType
from django.db.models import Q


def index(request):
	context = {}
	context['new_novel'] = NovelType.objects.all()[0].get_novels_by_cate()[:6]
	context["tuijian1"] = NovelType.objects.all()[:4]
	context["tuijian2"] = NovelType.objects.all()[4:8]
	context["all_type"] = NovelType.objects.all()
	print(context)
	return render(request,'feedfox/index.html',context)

# Create your views here.
def novel_list(request):
	context = {}
	context["novels"] = Novel.objects.all()
	#print(context["novels"])
	return render(request,'feedfox/novel_list.html',context)

def novel_detail(request,novel_id):
	context = {}
	context["all_type"] = NovelType.objects.all()
	if request.GET.get('articleId',0) == 0: #请求不带有章节参数
		context['novel'] = Novel.objects.get(id=novel_id)
		return render(request,'feedfox/chapters.html',context)
	else:
		context['article'] = Article.objects.get(id = request.GET.get('articleId',0))
		context['next_article'] = Article.objects.filter(id__gt=request.GET.get('articleId',0)).first()
		return render(request,'feedfox/article.html',context)

	
	#return HttpResponse("error")
	# return HttpResponse(str(novel_id)+"123")
def novel_cate(request,type_id):
	try:
		novel_type = NovelType.objects.get(id=type_id)
	except:
		novel_type = NovelType.objects.get(id=1)
	
	context = {}
	context['novel_type'] = novel_type
	context['novel_list'] = novel_type.get_novels_by_cate()[:6]
	context["all_type"] = NovelType.objects.all()
	return render(request,'feedfox/test.html',context)

def search(request):
	context = {}
	q = request.GET.get('key')
	if not q:
		context['error_msg'] = "请输入关键词"

	context['search_novels'] = Novel.objects.filter(Q(novel_name__icontains = q)|Q(author__icontains = q))
	
	return render(request,'feedfox/search_result.html',context)