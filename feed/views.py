from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import CreateCommentForm, CreatePostForm, EditPostForm
from .modals import DeletePostModal, PostModal
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
            return redirect('instaclone-post_view', new_post.id)
    form = CreatePostForm()
    return render(request, 'feed/createpost.html', {'form': form})


@login_required
def edit_post_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.user == post.creator:
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('instaclone-post_view', post.id)
        form = EditPostForm(instance=post)
        return render(request, 'feed/editpost.html', {'form': form, 'post': post})
    return redirect('instaclone-post_view', pk=pk)


@login_required
def post_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    modal = PostModal(iscreator=(post.creator == request.user))
    delete_post_modal = DeletePostModal(
        iscreator=(post.creator == request.user))
    blank_form = CreateCommentForm()
    context = {
        'post': post,
        'form': blank_form,
        'modal': modal,
        'delete_post_modal': delete_post_modal
    }
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    return render(request, 'feed/viewpost.html', context)


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
