import csv

from django.shortcuts import render
from django.views.generic import TemplateView


class InflationView(TemplateView):

    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        with open('inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data_list = [''.join(row).split(';') for row in reader]
            context = {'data': data_list}

        return render(request, self.template_name, context)

