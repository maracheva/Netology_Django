from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# возьмем функцию handle из базового кода и уберем проверку на валидацию
# https://github.com/django/django/blob/master/django/contrib/auth/management/commands/createsuperuser.py
class Command(BaseCommand):
	help = 'Create Superuser users and allow password to be provided'

	def handle(self, *args, **options):
		username = options.get('username')
		password = options.get()
		password2 = options.get('Password (again): ')
		# подключим к базе, но и без этого работает
		database = options.get('database')

		while password != password2:
			password2 = options.get("Error: Your passwords didn't match.")

		User.objects.create_superuser(username=username, email='', password=password)
		print('Superuser created successfully')

		# добавим в базу
		if password:
			user = self.UserModel._default_manager.db_manager(database).get(username=username)
			user.set_password(password)
			user.save()