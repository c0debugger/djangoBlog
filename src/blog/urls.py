from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from posts.views import category, index, blog, post, search

from filebrowser.sites import site #File Browser



urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls), #File Browser
    
    path('', index),
    path('blog/', blog, name = 'post_list'),
    path('blog/search/',search, name='search_results'),
    path('post/<id>/', post, name = 'post_detail'),
    path('blog/category/<title>/', category, name ='category_list'),

    path('tinymce/', include('tinymce.urls')),

    


    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)