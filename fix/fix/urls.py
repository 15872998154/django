"""fix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import carfix.views as cv 
import login.views as lv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', cv.book,name='book'),
    path('book/make_order',cv.make_order,name="make_order"),
    path("login/",lv.login,name="login"),
    path('logout/',cv.logout,name="logout"),
    path('register',lv.register,name='register'),
    # path('staff_info',cv.staff_info,name='staff_info'),
    # path("")
    path('delete_user',cv.delete_user,name="delete_user"),
    path('fix_list',cv.fix_list,name="fix_list"),
]
