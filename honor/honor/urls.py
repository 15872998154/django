
from django.urls import path
import honor.views as hv
urlpatterns = [
   
    path('', hv.index ,name = 'index'),
    path('raiders/<int:id>', hv.gonglue,name="gonglue"),
    path('skill/<int:id>',hv.skill,name='skill'),
]
