from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', info, name='info' ),
    path('post<int:post_id>/', show_post, name='post'),
    path('add-user/', add_user, name='add_user'),
    path('add-post/', add_post, name='addpost'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done', PasswordChangeDoneView.as_view(),  name='done'),
    path('register/', register, name='register')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
