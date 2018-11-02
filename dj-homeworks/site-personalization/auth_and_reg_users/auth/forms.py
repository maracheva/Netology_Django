from django import forms
from django.contrib.auth.models import User

# from django.contrib.auth.forms.UserCreationForm

from django.forms import Form, PasswordInput



class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30, error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label='Пароль', widget=PasswordInput, error_messages={'required': 'Укажите пароль'})

# регистрация с помощью своей формы
class RegistrationForm(Form):
    username = forms.CharField(label='Логин', max_length=30, error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label='Пароль', widget=PasswordInput, error_messages={'required': 'Укажите пароль'})
    password_again = forms.CharField(label='Пароль (еще раз)', widget=PasswordInput,
        error_messages={'required': 'Укажите пароль еще раз'})


    class Meta:
        model = User
        fields = ('username',)

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user


# регистрацию с помощью django.contrib.auth.forms.UserCreationForm.
class UserCreationForm(forms.ModelForm):
    pass