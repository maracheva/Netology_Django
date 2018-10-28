from django.views.generic import ListView

from .models import Student, Teacher


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    # def get_queryset(self):
    #     print(self.model.objects.all())
    #
    #     return self.model.objects.all()
    #

# class TeacherListView(ListView):
#     model = Teacher
#     ordering = 'subject'
#
#     def get_queryset(self):
#         print(self.model.objects.all())
#
#         return self.model.objects.all()