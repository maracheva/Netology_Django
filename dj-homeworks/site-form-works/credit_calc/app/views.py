from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import CalcForm


# В функции get проверяем данные формы c формы.
# Для этого передаем их в конструктор CalcForm(request.GET) и сохраняем в переменную.
# Затем проверяем валидность вызовом функции is_valid() формы.

class CalcView(TemplateView):
    template_name = 'app/calc.html'

    def get(self, request, *args, **kwargs):
        form = CalcForm(self.request.GET)

        if form.is_valid():
            cost = int(self.request.GET['initial_fee']) # сумма кредита
            rate = int(self.request.GET['rate']) # процентная ставка
            months_count = int(self.request.GET['months_count']) # срок кредита

            # Х = (стоимость + стоимость / процентную ставку)
            common_result = round(cost * (1 + 1/rate))
            # выплата в каждом месяце
            result = round(common_result / months_count)

            context = {
                'form': form,
                'common_result': common_result,
                'result': result
            }

            return render(request, self.template_name, context)


        return render(request, self.template_name, {'form': form})


