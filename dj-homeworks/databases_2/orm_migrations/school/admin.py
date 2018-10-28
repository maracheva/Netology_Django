from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'show_teachers')
    list_filter = ('group', 'teacher')  # добавляем фильтры в админку

    ordering = ['name'] # фильтр по алфавитному порядку

    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)  # фильтры в админку

    pass
