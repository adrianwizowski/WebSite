from django import template

register = template.Library()

@register.filter
def no2(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 40:
        return "foo green"
    elif value < 100:
        return "foo lightgreen"
    elif value < 150:
        return "foo yellow"
    elif value < 200:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def pm2(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 12:
        return "foo green"
    elif value < 36:
        return "foo lightgreen"
    elif value < 60:
        return "foo yellow"
    elif value < 84:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def pm10(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 20:
        return "foo green"
    elif value < 60:
        return "foo lightgreen"
    elif value < 100:
        return "foo yellow"
    elif value < 140:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def co(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 2:
        return "foo green"
    elif value < 6:
        return "foo lightgreen"
    elif value < 10:
        return "foo yellow"
    elif value < 14:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def so2(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 50:
        return "foo green"
    elif value < 100:
        return "foo lightgreen"
    elif value < 350:
        return "foo yellow"
    elif value < 500:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def o3(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 70:
        return "foo green"
    elif value < 120:
        return "foo lightgreen"
    elif value < 150:
        return "foo yellow"
    elif value < 180:
        return "foo orange"
    else:
        return "foo red"

@register.filter
def c6h6(value):
    value = value.replace(',','.')
    value = float(value)
    if value < 5:
        return "foo green"
    elif value < 10:
        return "foo lightgreen"
    elif value < 15:
        return "foo yellow"
    elif value < 20:
        return "foo orange"
    else:
        return "foo red"