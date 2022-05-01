from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_feed, name='instaclone-main_feed'),
    path('create/', views.create_post_view, name='instaclone-create_post_view'),
    path('view/', views.post_view, name='instaclone-post_view'),
    path('like/', views.like_view, name='instaclone-like_view'),
    path('unlike/', views.unlike_view, name='instaclone-unlike_view'),
]
