from django.urls import register_converter, path
from datetime import datetime
from .views import file_content, FileList


# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DatetimeConverter:
    regex = '[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'

    def to_python(self, value):
        date = datetime(value, "%Y-%m-%d").date()
        return date if date is not None else ''

    def to_url(self, value):
        return value

register_converter(DatetimeConverter, 'date_conver')

urlpatterns = [
    path('', FileList.as_view(), name='file_list'),
    path('<date_conver:date>', FileList.as_view(), name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
