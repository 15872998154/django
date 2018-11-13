from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .form import BookForm
from .models import Power,Car,User,FixList,Worker
import json
from django.http import JsonResponse
import django.contrib.auth as auth
from django.core.paginator import Paginator
# Create your views here.
def book(request):
    #无论何种方式访问该请求,如果用户未登陆,就重定向到登陆页面
    if not request.user.is_authenticated:
        return redirect('login')
    form = BookForm()
    
    #如果是post请求    
    if request.method == "POST":
        context = {}
        try:
            #对数据进行验证
            form = BookForm(request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['user_name']
                user_tel = form.cleaned_data['user_tel']
                user_addr = form.cleaned_data['user_addr']
                car_brand = form.cleaned_data['car_brand']
                car_broken_part = form.cleaned_data['car_broken_part']
                
                #验证通过创建表记录
                car = Car()
                car.car_brand = car_brand
                car.car_broken_part = car_broken_part
                car.save() #保存Car模型记录

                user = User()
                user.user_name = user_name
                user.user_tel = user_tel
                user.user_addr = user_addr
                user.user_car = car
                user.save() #保存User模型记录
            
                context['status'] = "success"
                context['count'] = len([ user for user in User.objects.all() if not user.is_made_order ])
                print("success"*10)
            
            # return HttpResponse(user_name+str(user_tel)+user_addr+car_brand+car_broken_part)
            else:
                form.add_error(None,'输入有误')
        except:
            context['status'] = "error"
            print("error"*10)
        return JsonResponse(context)         

            
            # return HttpResponse(user_name+str(user_tel)+user_addr+car_brand+car_broken_part)
    
    context={}
    context['form'] = form
    context['staff_info_id'] = Power.objects.get(user_name=request.user.username).id
    # print("=="*10)
    # print(Power.objects.get(user_name=request.user.username).query)
    # print("=="*10)
    # print(str(context['staff-info-id'])*50)
    context['is_boss'] = Power.objects.get(user_name=request.user.username).boss
    context['user_real_name'] = Power.objects.get(user_name=request.user.username).user_real_name
    context['waited_orders'] = [ user for user in User.objects.all() if not user.is_made_order ]
    
    return render(request,'carfix/book.html',context)


#待生成订单
def make_order(request):
    context={}
    #权限
    context['is_boss'] = Power.objects.get(user_name=request.user.username).boss
    #真实姓名
    context['user_real_name'] = Power.objects.get(user_name=request.user.username).user_real_name
    #取出所有用户
    

    context['waited_orders'] = [ user for user in User.objects.all()[::-1] if not user.is_made_order ]

    context["workers"] = Worker.objects.all()

    print(len(context['waited_orders']))
    return render(request,'carfix/make_order.html',context)


def logout(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    #登出
    auth.logout(request)
    
    print("logout"*10)
    return redirect('login') 

def delete_user(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}
    # if request.method == "POST":
    #     print("POST"*20)
    #     # User.objects.get(id = request.POST.get('id')).user_car.delete()
    #     print("=="*20)
    #     print(request.POST.get(id))
    #     print("=="*20)
    # print("delete"*20)
    # request.GET.get("user_id")
    
    try:
        User.objects.get(id = int(request.POST.get('user_id'))).user_car.delete()
        
         #store status

        context['deleted_id'] = request.POST.get('user_id') #transmit the infomation of deleted_user_id
        context['count'] = len([ user for user in User.objects.all() if not user.is_made_order ])
        print("ss"*10)
    
    except:

        context['status'] = "error"
        print("zz"*10)
    
    return JsonResponse(context)

def fix_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        #获取表单数据
        user_id = request.POST.get("user_id")
        main_broken_part = request.POST.get("main_broken_part")
        fix_man_id = request.POST.get("fix_man_id")
        bargain_price = request.POST.get("bargain_price")
        main_goods = request.POST.get("main_goods")
        
        user = User.objects.get(id=user_id)
        user.is_made_order = True
        user.save()
        
        fix_list = FixList()
        fix_list.user = User.objects.get(id=user_id)
        fix_list.user.is_made_order = True
        fix_list.price = bargain_price
        fix_list.worker = Worker.objects.get(id=fix_man_id)
        fix_list.main_goods = main_goods
        fix_list.save()



        return redirect('fix_list')


    
    context = {}
    #获取所有已完成订单
    # if request.method=="POST":
    #     user = request.user
    #     pass

    all_orders = FixList.objects.all()[::-1]
    print(str(len(all_orders))*100)
    paginator = Paginator(all_orders,8)
    context['paginator'] = paginator  
    
    try:
        num_page = request.GET.get("page",1)
        context["current_page_of_orders"] = paginator.page(num_page)
    except:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context["current_page_of_orders"] = paginator.page(1)
    # context['paginator'] = page


    context['is_boss'] = Power.objects.get(user_name=request.user.username).boss
    context['user_real_name'] = Power.objects.get(user_name=request.user.username).user_real_name
    context['waited_orders'] = [ user for user in User.objects.all() if not user.is_made_order ]
    return render(request,'carfix/all_orders.html',context)
    




