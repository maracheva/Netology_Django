import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    # value = cache.get('key')
    # cache.set('key', value)

    results = cache.get_or_set('key', [value.name for value in City.objects.all()])
    return JsonResponse(results, safe=False)


