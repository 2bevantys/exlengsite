from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, redirect

from .forms import RegisterUserForm, LoginUserForm
from .utils import *

menu = [{'title': "Таблица", 'url_name': 'words'},
        {'title': "Тест", 'url_name': 'test'},
        ]


def welcome(request):
    return render(request, 'words/welcome.html', {'menu': menu, 'title': 'Добро пожаловать'})


def index(request):
    return render(request, 'words/index.html', {'menu': menu, 'title': 'Страница words'})


def test(request):
    return render(request, 'words/test.html', {'menu': menu, 'title': 'Тестирование'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'words/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'words/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
