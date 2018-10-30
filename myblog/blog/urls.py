from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    #path('index/', views.index),
    path('article/<int:article_id>', views.article),
    path('article/update/<article_id>', views.update),
    path('create_article/', views.create_article),
    path('create_article/action/', views.create_article_action),
    path('article/update/action/', views.update_action),
]