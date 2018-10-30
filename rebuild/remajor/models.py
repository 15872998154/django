from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(primary_key = True)
    course_name = models.CharField(max_length = 32,verbose_name = "选修课程")
    course_teacher = models.CharField(max_length = 32,verbose_name = "授课教师")
    class Meta:
        verbose_name_plural = '选修课程管理'
    def __str__(self):
        return self.course_name
    def __setitem__(self, k, v):
                self.k = v

class Rebuild(models.Model):
    choice=(
        (1,'普通'),
        (2,'刷分'),
    )
    stu_id = models.CharField(max_length = 12,verbose_name = "学号")
    stu_name = models.CharField(max_length = 32,verbose_name = "姓名")
    profession = models.CharField(max_length = 32,verbose_name = "专业")
    course = models.ForeignKey('Course',on_delete = models.CASCADE,verbose_name = "重修课程")
    
    choice=models.IntegerField(choices=choice,verbose_name = "重修方式") #枚举类型
    class Meta:
        verbose_name_plural = '学生重修管理'
    def __str__(self):
        return str(self.stu_id) + self.stu_name

class Student(models.Model):
    stu_id  = stu_id = models.CharField(max_length = 12,verbose_name = "学号")
    stu_name = models.CharField(max_length = 32,verbose_name = "姓名")
    profession = models.CharField(max_length = 32,verbose_name = "专业")
    class Meta:
        verbose_name_plural = '学生管理'
    def __str__(self):
        return str(self.stu_id) + self.stu_name


   