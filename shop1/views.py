from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm, UserLoginForm, CommentForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    list_info = Index.objects.all()
    return render(request, 'shop1/index.html', {'list_info': list_info})


def portfolio(request, index_id):
    photo_index = Portfolio.objects.filter(index_id=index_id)
    paginator = Paginator(photo_index,6)
    page_num = request.GET.get('page',1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'shop1/portfolio.html', {'photo_index': photo_index, 'page_obj': page_obj})


def contacts(request):
    return render(request, 'shop1/contacts.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'shop1/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'shop1/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


#@login_required
def photo(request, id):
    photo_exz = Portfolio.objects.get(pk=id)
    comments = Comment.objects.filter(post=photo_exz)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = photo_exz
            comment.save()
            return redirect('index')


    else:
        form = CommentForm()

    return render(request, 'shop1/photo.html', {'photo_exz': photo_exz, 'comments': comments, 'form': form})


