from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from blog.forms import LoginForm
from django.urls import reverse
def userlogin(request):
    if request.method =='POST':#如果是POST请求就提交表单
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = auth.authenticate(request,username=username,password=password)
            if user is not None:#如果是真实用户
                auth.login(request,user)#用户登录
                #return redirect(request.GET.get('from',reverse('home')))
                return redirect(request.GET.get('from',reverse('home')))
            else:
                loginform.add_error(None,'用户名或密码不正确')#不是
                
    else:#如果是GET请求就加载数据
        loginform = LoginForm()
    
    context = {}
    context['loginform'] = loginform
    return render(request,'blog/login.html',context)