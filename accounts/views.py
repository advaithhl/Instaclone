from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def empty_path(request):
    return redirect('instaclone-accounts_login')


def login_view(request):
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instaclone-accounts_login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
