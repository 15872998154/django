from django.shortcuts import render,HttpResponse,redirect
from .models import Course,Rebuild,Student
from django.forms.models import model_to_dict  
from django.http import JsonResponse
# Create your views here.
def remajor(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        #取的学号
        stu_id = request.user.username
        #取得姓名
        stu_name = Student.objects.get(stu_id=stu_id).stu_name
        #取得专业
        profession = Student.objects.get(stu_id=stu_id).profession
        #取得课程
        course = Course.objects.get(course_id = request.POST.get('course_id'))
        #取得重修方式
        choice = 1 if request.POST.get('con')=='nomal' else  2
        print(choice)
        #判断表中是否有该记录
        if len(Rebuild.objects.filter(stu_id=stu_id,stu_name=stu_name,
                profession=profession, course=course,choice=choice))>0:
                return HttpResponse('请勿重复提交数据,刷新网页后重试')

        Rebuild(stu_id=stu_id,stu_name=stu_name,
                profession=profession, course=course,choice=choice).save()
        return HttpResponse('报名成功')

    all_courses = Course.objects.all() #获取所有课程清单
    
    remajor_courses = []  #存储该名学生重修课程
    
    records = Rebuild.objects.all() 
    for record in records:
        if record.stu_id == request.user.username:
            remajor_courses.append(record.course) #如果发现该学生有重修记录就将其记入该学生的重修课程中
    
    context = {}
    context['all_courses'] = all_courses
    #获取姓名
    stu_name = Student.objects.get(stu_id=request.user.username).stu_name
    
    context['stu_name'] = stu_name
    context['remajor_courses'] = remajor_courses
    
    return render(request,'remajor/remajor.html',context)

def drop(request):#退课
    course = request.POST.get('course_id')
    print(request.POST.get('course_id'))
    
    course = Course.objects.get(course_id=request.POST.get('course_id'))
    if len(Rebuild.objects.filter(stu_id=request.user.username,course=course))==0:
        return HttpResponse('请勿重复提交数据,刷新网页后重试')
    
    Rebuild.objects.get(stu_id=request.user.username,course=course).delete()
    print('删除成功！')
    return HttpResponse('退课成功')
    


