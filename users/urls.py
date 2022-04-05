from django.urls import path

from . import views

urlpatterns = [
    path('', views.empty_path, name='instaclone-accounts_empty'),
    path('login/', views.login_view, name='instaclone-accounts_login'),
]
