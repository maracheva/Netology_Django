import csv

from urllib.parse import urlencode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from .settings import BUS_STATION_CSV
# from django.conf import settings

# чтение csv файла
station_list = [] # создадим пустой список, который будем потом использовать как object_list пагинации
with open(BUS_STATION_CSV, newline='',  encoding='cp1251') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			station_list.append({
				'Name': row['Name'],
				'Street': row['Street'],
				'District': row['District']
				})


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    # Импортируем Paginator и разбиваем object_list на queryset по 10 объектов на страницу.
    # Через переменную paginator обращаемся к пагинатору Django
    paginator = Paginator(station_list, 10)
    page = request.GET.get('page') # создаем переменную = GET запросу по параметру 'page'

    # Формируем исключения
    try:
        post = paginator.page(page) # current page
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        post = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results.
        post = paginator.page(paginator.num_pages)


    return render_to_response('index.html', context={
        'bus_stations': post.object_list, # список элементов объекта на странице
        'current_page': page, # текущая страница
        'prev_page_url': ('?'.join([reverse(bus_stations), urlencode(
            {'page': post.previous_page_number()})])) if post.has_previous() else False,
        'next_page_url': ('?'.join([reverse(bus_stations), urlencode(
        {'page': post.next_page_number()})])) if post.has_next() else False,

    })

