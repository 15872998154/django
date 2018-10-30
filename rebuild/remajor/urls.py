
from django.urls import path
import remajor.views as rv
# # from login.views import login
# import login.urls

urlpatterns = [
    path('',rv.remajor,name="remajor"),
    path('drop/',rv.drop,name="drop"),


    
   
]
