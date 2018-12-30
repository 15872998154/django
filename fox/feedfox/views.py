from django.shortcuts import render,HttpResponse
from .models import Article,Novel
# Create your views here.
def novel_list(request):
	context = {}
	context["novels"] = Novel.objects.all()
	#print(context["novels"])
	return render(request,'feedfox/novel_list.html',context)

def novel_detail(request,novel_id):
	context = {}
	if request.GET.get('articleId',0) == 0: #请求不带有章节参数
		context['novel'] = Novel.objects.get(id=novel_id)
		return render(request,'feedfox/novel_detail.html',context)
	else:
		context['article'] = Article.objects.get(id = request.GET.get('articleId',0))
		return render(request,'feedfox/article.html',context)

	
	#return HttpResponse("error")
	# return HttpResponse(str(novel_id)+"123")
