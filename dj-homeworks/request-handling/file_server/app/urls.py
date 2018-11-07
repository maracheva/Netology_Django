from django.urls import register_converter, path
from datetime import datetime
from .views import file_content, FileList
import re

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DateConverter:
    regex = '[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'

    def to_python(self, value):
        # преобразуем дату в формат date_string
        date = datetime.strptime(value, "%Y-%m-%d").date()
        return date if date is not None else ''


    def to_url(self, value):
        return value.date()

register_converter(DateConverter, 'date_conver')

urlpatterns = [
    path('', FileList.as_view(), name='file_list'),
    path('<date_conver:date>', FileList.as_view(), name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
