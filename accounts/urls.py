from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.empty_path, name='instaclone-accounts_empty'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='instaclone-accounts_login'),
    path('register/', views.register_view, name='instaclone-accounts_register'),
]
