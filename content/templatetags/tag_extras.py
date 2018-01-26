from django import template

register = template.Library()

def discription(value, parametr, levels):
    if value < levels[0]:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': levels[4]}
        return dictonary[str(parametr)]
    elif value < levels[1]:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': levels[4]}
        return dictonary[str(parametr)]
    elif value < levels[2]:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': levels[4]}
        return dictonary[str(parametr)]
    elif value < levels[3]:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': levels[4]}
        return dictonary[str(parametr)]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': levels[4]}
        return dictonary[str(parametr)]

@register.filter
def time(time):
    return str(time)

@register.simple_tag(name='my_tag')
def my_tag(key, value, parametr):
    if key == 'pm25':
        levels= [12, 36, 60, 84, "Pył zawieszony 2.5µm"]
        return discription(value, parametr, levels)
    if key == 'pm10':
        levels = [20, 60, 100, 140 , "Pył zawieszony 10µm"]
        return discription(value, parametr, levels)
    if key == 'no2':
        levels = [40, 100, 150, 200, "Dwutlenek azotu"]
        return discription(value, parametr, levels)
    if key == 'co':
        levels = [2000, 6000, 10000, 14000, "Tlenek węgla"]
        return discription(value, parametr, levels)
    if key == 'so2':
        levels = [50, 100, 350, 500, "Dwutlenek siarki"]
        return discription(value, parametr, levels)
    if key == 'o3':
        levels = [70, 120, 150, 180, "Ozon"]
        return discription(value, parametr, levels)