from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(urls)),
    path('blog/', include(urls)),
    path('blog/', include(urls)),
    path('blog/', include(urls)),


]