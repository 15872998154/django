from django.db import models

# Create your models here.
class Student(models.Model):
	stu_name = models.CharField(max_length = 32)
	stu_age = models.IntegerField()
	score = models.IntegerField()

