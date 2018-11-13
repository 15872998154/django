from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Student
# Create your views here.
def stu_list(request):
	context = {}
	context['students'] =  Student.objects.all()
	return render(request,'student/list.html',context)


def delete(request):
	try:

		Student.objects.get(id = request.POST['user_id']).delete()
		return JsonResponse({"stauts":"success"}) 
	except:
		return JsonResponse({"stauts":"faith"})

	

def modify(request):
	stu_id = request.POST['stu_id']
	name = request.POST['name']
	age = request.POST['age']
	score = request.POST['score']
	context = {}
	try:
		modify_student = Student.objects.get(id=stu_id)
		modify_student.stu_name = name
		modify_student.stu_age = age
		modify_student.score = score
		modify_student.save()
		context['id'] = stu_id
		context['stu_name'] = name
		context['age'] = age
		context['score'] = score
		context['status'] = "success"

	except:
		context["status"] = "error"
		context["error_msg"] = "用户密码不对"

	return JsonResponse(context)