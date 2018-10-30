from django.shortcuts import render,HttpResponse,redirect,reverse
from .form import UserForm
import django.contrib.auth as auth
# from django.template import RequestContext 
# from .tools import Test
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST) #实例化一个form表单对象
        if form.is_valid():  #检测数据格式是否合法
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request,username=username,password=password)
            if user is not None: 
                auth.login(request,user)
                return redirect('/remajor')
                #return HttpResponse('hello')
            else: #用户名或者密码不正确
                form.add_error(None,'用户名或密码不正确')
                
    else:#get 方式请求
        form = UserForm()
    #return render(request,"login/form.html")
    context = {}
    context['form'] = form
    return render(request,'login/form1.html',context)
    #return render(request, 'login/form1.html',{'form':UserForm()})
