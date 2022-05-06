from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from feed.forms import CreatePostForm

from .models import Post


def redirect_to_feed(request):
    return redirect('instaclone-main_feed')


@login_required
def main_feed(request):
    posts = Post.objects.filter(creator=request.user.id)
    return render(request, 'feed/home.html', {'posts': posts})


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.save()
            form.save_m2m()
            return redirect('instaclone-main_feed')
    form = CreatePostForm()
    return render(request, 'feed/createpost.html', {'form': form})


@login_required
def post_view(request, pk):
    post = Post.objects.filter(id=pk).first()
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
