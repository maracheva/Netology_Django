import os
from datetime import datetime
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from .settings import FILES_PATH


class FileList(TemplateView):
    template_name = 'index.html'

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    def get_context_data(self, date=None):
        file_list = []

        for file in os.listdir(FILES_PATH):
            # os.stat возвращает именованный кортеж с атрибутами st_mtime и st_ctime
            path_to_file = os.stat(os.path.join(FILES_PATH, file))
            # дата создания файла (из стандартного представления времени)
            data_file = datetime.fromtimestamp(int(path_to_file.st_ctime)).date()
            # print(data_file)

            if date == None or data_file <= date:
                file_list.append(
                    {'name': file,
                     'ctime': datetime.fromtimestamp(int(path_to_file.st_ctime)).date(), # последний раз, когда были изменены атрибуты файла (разрешения, имя и т.д.)
                     'mtime': datetime.fromtimestamp(int(path_to_file.st_mtime)).date() #  последний раз, когда было изменено содержание файла
                     })

        return {'files':  file_list,
                'date': date # Этот параметр необязательный
        }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(FILES_PATH, name), encoding='utf-8') as file:
        data = file.read()

    return render_to_response('file_content.html', context={'file_name': name, 'file_content': data})

