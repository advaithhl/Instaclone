from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    fullname = forms.CharField(max_length=70, label='Full Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'password1', 'password2']

    @staticmethod
    def split_full_name(fullname):
        """
        John Will Smith -> ['John', 'Will Smith']
        """
        split_name = fullname.split(' ')
        return [split_name[0], ' '.join(split_name[1:])]

    def save(self, commit=True):
        clean_fullname = self.cleaned_data.get('fullname')
        first_name, last_name = UserRegisterForm.split_full_name(
            clean_fullname)
        self.instance.first_name = first_name
        self.instance.last_name = last_name
        super(UserRegisterForm, self).save(commit)
