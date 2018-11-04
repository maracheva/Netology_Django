# import django.contrib.auth.forms.UserCreationForm

from django import forms
from django.contrib.auth.models import User
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


# регистрация с помощью django.contrib.auth.forms.UserCreationForm.
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('user',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user