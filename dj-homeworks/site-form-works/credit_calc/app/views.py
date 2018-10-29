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
            cost = int(self.request.GET['initial_fee'])
            rate = int(self.request.GET['rate'])
            months_count = int(self.request.GET['months_count'])

            # Х = (стоимость + стоимость * процентную ставку) / срок в месяцах.
            total_cost = round((cost + cost * rate) / months_count)
            result = round(total_cost / 12)

            context = {
                'form': form,
                'common_result': total_cost,
                'result': result
            }

            return render(request, self.template_name, context)


        return render(request, self.template_name, {'form': form})


