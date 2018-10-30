
from django.contrib import admin
from django.urls import path,include
import blog.views as bv
import blog.urls
from django.conf import settings
from django.conf.urls.static import static
import comment.urls     
from . import views     


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bv.home,name = "home"),
    path('blog/', include(blog.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('comment_login/',bv.comment_login,name = "comment_login"),
    path("comment/",include(comment.urls)),
    path("userlogin/",views.userlogin,name = "userlogin")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)