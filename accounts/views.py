from django.shortcuts import redirect, render


def empty_path(request):
    return redirect('instaclone-accounts_login')


def login_view(request):
    return render(request, 'accounts/login.html')
