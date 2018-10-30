from django.db import models

# Create your models here.
class Article(models.Model):
	
	title = models.CharField(max_length = 32)

	content = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.content