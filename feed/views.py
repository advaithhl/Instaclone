from django.shortcuts import render


def main_feed(request):
    return render(request, 'feed/home.html')
