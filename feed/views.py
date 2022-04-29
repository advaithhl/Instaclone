from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Post


@login_required
def main_feed(request):
    posts = Post.objects.filter(creator=request.user.id)
    return render(request, 'feed/home.html', {'posts': posts})


@login_required
def post_view(request):
    post_id = request.GET['id']
    post = Post.objects.filter(id=post_id).first()
    return render(request, 'feed/viewpost.html', {'post': post})


@login_required
def like_view(request):
    user = request.user
    post_id = request.GET['id']
    post = Post.objects.filter(id=post_id).first()
    post.liked_users.add(user)
    return JsonResponse({'status': 'ok'})


@login_required
def unlike_view(request):
    user = request.user
    post_id = request.GET['id']
    post = Post.objects.filter(id=post_id).first()
    post.liked_users.remove(user)
    return JsonResponse({'status': 'ok'})
