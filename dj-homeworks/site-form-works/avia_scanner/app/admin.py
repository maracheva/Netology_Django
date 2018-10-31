from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ['name'] # сортируем в алфавитном порядке

admin.site.register(City, CityAdmin)
