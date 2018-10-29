from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    # rate = forms.CharField(label="Процентная ставка") ???? зачем здесь поле CharField ????
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee



    def clean(self):
        # Вызов super().clean() гарантирует, что любая логика проверки в родительских классах поддерживается.
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')
        months_count = cleaned_data.get('months_count')

        msg = 'Этот параметр не может быть отрицательным' # Сообщение ошибки
        if not rate or rate < 1:
            self.add_error('rate', msg)
        if not months_count or months_count < 1:
            # raise forms.ValidationError(msg)
            self.add_error('months_count', msg)


        return self.cleaned_data

    # Так же надо проверить поля.
    # Если ожидаются только цифры, то forms.CharField излишен.
    # def validate_even(value):
    #     if value is not int:
    #         raise ValidationError(_('тут должно быть число'), params={'value': value}, )
