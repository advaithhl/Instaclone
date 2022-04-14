from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def main_feed(request):
    return render(request, 'feed/home.html')
