from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from .models import Blog,BlogType,ReadNum
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from .forms import LoginForm
# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def blog_list(request):
    all_blogs = Blog.objects.all()
    context = {}
    
    paginator = Paginator(all_blogs,4)
    page_num = request.GET.get('page',1)#获取页码参数
    page_of_blogs = paginator.get_page(page_num)
    
    current_page = page_of_blogs.number
    page_range = list(range(max(current_page-2,1),min(current_page+3,page_of_blogs.paginator.num_pages)))
    if page_range[0] >= 3:
        page_range.insert(0,"...")
    if page_range[-1] <= page_of_blogs.paginator.num_pages-2:
        page_range.append("...")
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != page_of_blogs.paginator.num_pages:
        page_range.append(page_of_blogs.paginator.num_pages)

    date_count_dict={}    
    blog_dates = Blog.objects.dates('created_time','month',order='DESC')
    for blog_date in blog_dates:
        count = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        date_count_dict[blog_date] = count
    context['blog_dates'] = blog_dates
    context['blog_types'] = BlogType.objects.all()
    #context['all_blogs'] = all_blogs
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['date_count_dict'] = date_count_dict

    return render(request,'blog/blog_list.html',context)

def blog_detail(request,blog_id):
    context = {}
    blog = get_object_or_404(Blog,pk = blog_id)
    if not request.COOKIES.get('blog_{}'.format(blog.pk)):
        read = ReadNum.objects.filter(blog=blog).first()
        read.count += 1
        read.save()
    else:
        read = ReadNum.objects.filter(blog=blog).first()
    read_count = read.count
    #print(read.count) 
    context['read_count'] = read_count   
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog

    content_type = ContentType.objects.get(model = 'blog')
    context['comments'] = Comment.objects.filter(content_type = content_type,object_id = blog_id)

    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie('blog_{}'.format(blog.pk),'true')
    return response

def blogs_with_type(request,type_id):
    context = {}
    selected_type = get_object_or_404(BlogType,pk = type_id)
    all_blogs = Blog.objects.filter(blog_type = selected_type)
    

    paginator = Paginator(all_blogs,4)
    page_num = request.GET.get('page',1)#获取页码参数
    page_of_blogs = paginator.get_page(page_num)
    
    current_page = page_of_blogs.number
    page_range = list(range(max(current_page-2,1),min(current_page+3,page_of_blogs.paginator.num_pages)))
    if page_range:
        if page_range[0] >= 3:
            page_range.insert(0,"...")
        if page_range[-1] <= page_of_blogs.paginator.num_pages-2:
            page_range.append("...")
        if page_range[0] != 1:
            page_range.insert(0,1)
        if page_range[-1] != page_of_blogs.paginator.num_pages:
            page_range.append(page_of_blogs.paginator.num_pages)

    #blog_dates = Blog.objects.dates('created_time','month',order='DESC')
    #print(blog_dates)
    date_count_dict={}    
    blog_dates = Blog.objects.dates('created_time','month',order='DESC')
    for blog_date in blog_dates:
        count = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        date_count_dict[blog_date] = count
    context['blog_dates'] = blog_dates
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['spicifical_type'] = selected_type
    context['blog_types'] = BlogType.objects.all()
    context['date_count_dict'] = date_count_dict
    return render(request,'blog/blogs_with_type.html',context)
    #return render_to_response('blog/index.html')

def blogs_with_date(request,year,month):
    context = {}
    all_blogs = Blog.objects.filter(created_time__year = year,created_time__month = month)
    paginator = Paginator(all_blogs,4)
    page_num = request.GET.get('page',1)#获取页码参数
    page_of_blogs = paginator.get_page(page_num)
    
    current_page = page_of_blogs.number
    page_range = list(range(max(current_page-2,1),min(current_page+3,page_of_blogs.paginator.num_pages)))
    if page_range:
        if page_range[0] >= 3:
            page_range.insert(0,"...")
        if page_range[-1] <= page_of_blogs.paginator.num_pages-2:
            page_range.append("...")
        if page_range[0] != 1:
            page_range.insert(0,1)
        if page_range[-1] != page_of_blogs.paginator.num_pages:
            page_range.append(page_of_blogs.paginator.num_pages)

    #博客分类 日期归档 所有按日期分类的博客
    #blog_dates = Blog.objects.dates('created_time','month',order='DESC')
    date_count_dict={}    
    blog_dates = Blog.objects.dates('created_time','month',order='DESC')
    for blog_date in blog_dates:
        count = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        date_count_dict[blog_date] = count

    context['specific_date'] = all_blogs[0].created_time
    context['blog_dates'] = blog_dates
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    context['date_count_dict'] = date_count_dict
    #return render_to_response('blog/index.html')
    return render(request,'blog/blogs_with_date.html',context)

def comment_login(request):
    """username = request.POST.get('username',"")
    password = request.POST.get('password',"")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        previous_page = request.META.get('HTTP_REFERER',reverse('home'))
        return redirect(previous_page)
    else:
        return render(request,'blog/unlogined_page.html',{'message':"登录错误"})
    """
    context = {}
    loginform = LoginForm()
    context['loginform'] = loginform
    return render(request,'blog/login.html',context)
