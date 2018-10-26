from django import template
from datetime import datetime


register = template.Library()

@register.filter
# форматирует дату
def format_date(value):
    # получим разницу в минутах
    delta = (datetime.timestamp(datetime.now()) - value) / 60
    # Если пост был меньше 10 минут назад, пишет "только что"
    if delta < 10:
        return 'только что'
    # Если пост был меньше 24 часов назад, пишет "X часов назад"
    if (delta / 60) < 24:
        return f'{round(delta / 60)} часов назад'
    # Если пост был больше 24 часов назад, выводит дату в формате "Год-месяц-число"
    return datetime.fromtimestamp(value).date().strftime("%Y-%m-%d")

# форматирование поля score, рейтинг
@register.filter
def format_num_score(value, default):
    # Если поле score отсутствует, то рендерится дефолтное значение, которое передается в качестве параметра фильтра.
    if value is None:
        value = default
    if value  <= -5:
        return 'все плохо'
    if  -5 < value < 5:
        return 'нейтрально'
    if value >= 5:
        return 'хорошо'


# форматирование поля comments
@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    if  0 < value < 50:
        return value
    if value >= 50:
        return '50+'

# форматирование поля текста
@register.filter
def format_selftext(value, count):
    # Оставляет count первых и count последних слов, между ними должно быть троеточие.
    # count задается параметром фильтра. Знаки препинания остаются, обрезаются только слова.
    if value:
        new_value = ' '.join(value.split()[:count] + ['...'] + value.split()[-count:])
        return new_value

    return value
