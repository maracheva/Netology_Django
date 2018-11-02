from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
# from django.contrib.auth.forms.UserCreationForm


from django.shortcuts import render

# @login_required(login_url='/accounts/login/')
def home(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)

    # user = request.user
    # context = {}
    # if user is not None:
    #     # Redirect to a success page.
    #     if user.is_authenticated:
    #         context['user'] = user
    #     else:
    #         context['user'] = False
    # return render(request, 'home.html', {'context': context})
    #
    # # if user is not None:
    # #     login(request, user)
    # #     # Redirect to a success page.
    # #     ...
    # # # else:
    # #     # Return an 'invalid login' error message.
    # #
    return render(request, 'home.html')


def signup(request):
    return render(
        request,
        'signup.html'
    )

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return render('Authenticated successfully')
                    return home(request)
                else:
                    return render(request, 'account/login.html', {'form': form, 'error': 'Аккаунт неактивен'})
            else:
                return render(request, 'account/login.html', {'form': form, 'error': 'Не верный логин или пароль!'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    logout(request)
    return render(request, 'account/logout.html')