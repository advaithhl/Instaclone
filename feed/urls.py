from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_feed, name='instaclone-main_feed'),
    path('view/', views.post_view, name='instaclone-post_view'),
]
