from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


# должна открыться страница с формой для регистрации с тремя полями (логин, пароль и подтверждение пароля)
def user_signup(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        # проверка на валидацию формы
        if user_form.is_valid():
            # перейти на страницу успешной регистрации
            return render(request, 'accounts/signup_finish.html', {'user_form': user_form})
            # return HttpResponse('Регистрация прошла успешно!')
    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form})


# должна открыться страница с формой для авторизации с двумя полями (логин и пароль)
# @login_required(login_url='/accounts/login/')
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return home(request)
                else:
                    return render(request, 'accounts/login.html', {'form': form, 'error': 'Аккаунт неактивен'})
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Не верный логин или пароль!'})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')