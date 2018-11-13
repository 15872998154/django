
from django.urls import path
from login import views as lv
urlpatterns = [
    
    path('',lv.login, name="login")
]
