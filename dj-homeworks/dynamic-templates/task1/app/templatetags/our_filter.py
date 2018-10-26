from django import template

register = template.Library()


@register.filter
def give_color_cell(value, cell):
    if cell == 0:
        return ''
    if cell == 13:
        return '#808080'

    if value:
        value = float(value)
        if value < 0:
            return '#008000'
        if 1 < value <= 2:
            return '#ff0000'
        if 2 < value <= 5:
            return '#f8809c'
        if 5 < value:
            return '#f8b0c0'

    return ''
