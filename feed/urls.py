from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_feed, name='instaclone-main_feed'),
    path('create/', views.create_post_view, name='instaclone-create_post_view'),
    path('view/<int:pk>/', views.post_view, name='instaclone-post_view'),
    path('view/', views.redirect_to_feed, name='instaclone-view_empty'),
    path('edit/<int:pk>/', views.edit_post_view, name='instaclone-edit_post_view'),
    path('edit/', views.redirect_to_feed, name='instaclone-edit_post_view'),
    path('delete/<int:pk>/', views.delete_post_view, name='instaclone-delete_post_view'),
    path('delete/', views.redirect_to_feed, name='instaclone-edit_post_view'),
    path('like/', views.like_view, name='instaclone-like_view'),
    path('unlike/', views.unlike_view, name='instaclone-unlike_view'),
]
