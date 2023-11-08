from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', info, name='info' ),
    path('post<int:post_id>/', show_post, name='post'),
    path('add-user/', add_user, name='add_user'),
    path('add-post/', add_post, name='addpost')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
