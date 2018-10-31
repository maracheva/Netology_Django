
import datetime

from django import forms
from django.forms import SelectDateWidget
from .widgets import AjaxInputWidget, Calendar
from .models import City



class SearchTicket(forms.Form):
    # форма города отправления AjaxInputWidget
    city_from = forms.CharField(label='Город отправления', label_suffix=':',
                                widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}))
    # форма города прибытия
    # для того чтобы задать сортировку данных на сайте будем использовать forms.ChoiceField с параметром choices

    # через генератор списка
    cities_list = [(id, val.name) for id, val in enumerate(City.objects.all().order_by('name'))]

    city_to = forms.ChoiceField(label='Город прибытия', label_suffix=':', widget=forms.Select(), choices=(cities_list),
                                initial='0')

    #  ТАК НЕ СРАБОТАЛО
    # city_to = forms.ChoiceField(label='Город прибытия', label_suffix=':', initial='0', widget=forms.Select(), )
    #
    # def __init__(self, *args, **kwargs):
    #     super(SearchTicket, self).__init__(*args, **kwargs)
    #
    #
    #     for val in City.objects.all().order_by('name'):
    #         self.fields['city_to'].choices.append((val.id + 1, val.name))


    # форма для выбора даты
    MONTHS = {
        1: ('Январь'), 2: ('Февраль'), 3: ('Март'), 4: ('Аперль'),
        5: ('Май'), 6: ('Июнь'), 7: ('Июль'), 8: ('Август'),
        9: ('Сентябрь'), 10: ('Октябрь'), 11: ('Ноябрь'), 12: ('Декабрь')
    }

    year = datetime.date.today().year
    '''
    зададим необязательные параметры years, months:
    years = range(year, year + 2) - выбор годов (2018б 2019), иначе по умолчанию будет список, 
                                    содержащий текущий год и следующие 9 лет. 
    
    months=MONTHS - зададим название месяцев в кириллице, по умолчанию - латиница
    
    '''

    start_date = forms.DateField(label='Туда', label_suffix=':', initial=datetime.date.today,
                                 widget=forms.SelectDateWidget(empty_label="Nothing",
                                                      years=range(year, year+2), months=MONTHS))

    # end_date = forms.DateField(label='Обратно', label_suffix=':', initial=datetime.date.today,
    #                            widget=forms.SelectDateWidget(empty_label="Nothing",
    #                                                   years=range(year, year+2), months=MONTHS))

    # через загруженный виджет
    end_date = forms.DateField(label='Обратно', label_suffix=':', widget=Calendar())
