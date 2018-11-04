# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# создание пользователя
user = User.objects.create_user('username', 'user@domain.name', 'password')

# class User(AbstractUser):
#     pass


