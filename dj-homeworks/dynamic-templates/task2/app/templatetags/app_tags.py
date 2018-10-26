from django import template

register = template.Library()

# @register.inclusion_tag('app/base.html') # регистрируем тег и подключаем шаблон
# # def show_active(value):
# #     context = {'page': value}
# #     return context

@register.simple_tag
def show_active(request, pattern):
    path = request.path
    if path == pattern:
        return 'active'
    return ''
