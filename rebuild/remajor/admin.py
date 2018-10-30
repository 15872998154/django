from django.contrib import admin
from .models import Rebuild,Course,Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id','stu_name','profession')
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','course_name','course_teacher')


@admin.register(Rebuild)
class RebuildAdmin(admin.ModelAdmin):
    # 需要展示的字段
    list_display = ('id', 'stu_id', 'stu_name','profession','course','choice')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('stu_id', 'stu_name', 'course','profession','choice')
    list_per_page = 50 #每页显示的最大记录数
    ordering = ('stu_id',)#排序规则，倒叙添- 例如 '-stu_id'
    list_filter =('course', 'profession') #过滤器
    search_fields =('stu_id', 'stu_name','course__course_name','profession') #搜索字段
    fields = ('stu_id', 'stu_name', 'course__course_name','profession','choice' )#显示可以修改的字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选　
# 注册时，在第二个参数写上 admin model
# admin.site.register(Rebuild, RebuildAdmin)
# admin.site.register(Rebuild, RebuildAdmin)


admin.site.site_header = "武汉工程大学邮电与信息工程学院重修管理系统" 
admin.site.site_title = "重修管理系统"

