from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post


@login_required
def main_feed(request):
    posts = Post.objects.filter(creator=request.user.id)
    return render(request, 'feed/home.html', {'posts': posts})
