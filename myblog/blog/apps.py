from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    def __str__(self):
    	return self.title
