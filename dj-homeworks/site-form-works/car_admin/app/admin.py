from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'get_reviews') # выводим наименование парметров
    list_filter = ('brand', 'model')  # фильтры в админку
    ordering = ('pk',) # сортируем вывод объектов в списке по порядку добавления

    search_fields = ('brand', 'model') # поиск в админке по моделям или бренду


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    list_filter = ('car', 'title')  # фильтры в админку

    search_fields = ('title', 'car__model',) # поиск в админке по наименованию и модели


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
