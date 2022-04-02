from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_feed, name='instaclone-main_feed'),
]
