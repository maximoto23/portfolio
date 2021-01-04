from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email adress', widget=forms.EmailInput(attrs={'class': "form-control", 'rows': 5}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': "form-control"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'text': forms.TextInput(attrs={'class': "form-control"}),
        }