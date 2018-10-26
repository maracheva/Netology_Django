from django.urls import register_converter, path
from datetime import datetime
from .views import file_content, FileList


# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DatetimeConverter:
    regex = '[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'

    def to_python(self, value):
        # result = datetime(value.year, value.month, value.day).date()
        result = datetime.strptime(value, "%Y-%m-%d").date()
        return result if result is not None else ''

    def to_url(self, value):
        return value.date()


register_converter(DatetimeConverter, 'date_conver')

urlpatterns = [# Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    path('', FileList.as_view(), name='file_list'),  # отображение списка файлов
    path('<date_conver:date>', FileList.as_view(), name='file_list'),
    # отображение списка файлов с фильтрацией по дате /2018-01-01/
    path('file/<str:name>', file_content, name='file_content'),  # отображение отдельных файлов /file_name.txt
]
