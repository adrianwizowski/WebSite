from django import template

register = template.Library()

@register.filter
def no2(value, parametr):
    if value < 40:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Dwutlenek azotu"}
        return dictonary[parametr]
    elif value < 100:
        dictionary = {"color": "#00ff00", "quality": "Dobra", "disc": "Dwutlenek azotu"}
        return dictionary[parametr]
    elif value < 150:
        dictionary = {"color": "#ffff99", "quality": "Umiarkowana", "disc": "Dwutlenek azotu"}
        return dictionary[parametr]
    elif value < 200:
        dictionary = {"color": "#ffd633", "quality": "Dostateczna", "disc": "Dwutlenek azotu"}
        return dictionary[parametr]
    else:
        dictionary = {"color": "#cc0000", "quality": "Zła", "disc": "Dwutlenek azotu"}
        return dictionary[parametr]

@register.filter
def pm2(value, parametr):
    if value < 12:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Pył zawieszony 2.5µm"}
        return dictonary[str(parametr)]
    elif value < 36:
        dictionary = {"color": "#00ff00", "quality": "Dobra", "disc": "Pył zawieszony 2.5µm"}
        return dictionary[str(parametr)]
    elif value < 60:
        dictionary = {"color": "#ffff99", "quality": "Umiarkowana", "disc": "Pył zawieszony 2.5µm"}
        return dictionary[str(parametr)]
    elif value < 84:
        dictionary = {"color": "#ffd633", "quality": "Dostateczna", "disc": "Pył zawieszony 2.5µm"}
        return dictionary[str(parametr)]
    else:
        dictionary = {"color": "#cc0000", "quality": "Zła", "disc": "Pył zawieszony 2.5µm"}
        return dictionary[str(parametr)]

@register.filter
def pm10(value, parametr):
    if value < 20:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Pył zawieszony 10µm"}
        return dictonary[parametr]
    elif value < 60:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': "Pył zawieszony 10µm"}
        return dictonary[parametr]
    elif value < 100:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': "Pył zawieszony 10µm"}
        return dictonary[parametr]
    elif value < 140:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': "Pył zawieszony 10µm"}
        return dictonary[parametr]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': "Pył zawieszony 10µm"}
        return dictonary[parametr]

@register.filter
def co(value, parametr):
    if value < 2000:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Tlenek węgla"}
        return dictonary[parametr]
    elif value < 6000:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': "Tlenek węgla"}
        return dictonary[parametr]
    elif value < 10000:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': "Tlenek węgla"}
        return dictonary[parametr]
    elif value < 14000:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': "Tlenek węgla"}
        return dictonary[parametr]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': "Tlenek węgla"}
        return dictonary[parametr]

@register.filter
def so2(value, parametr):
    if value < 50:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Dwutlenek siarki"}
        return dictonary[parametr]
    elif value < 100:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': "Dwutlenek siarki"}
        return dictonary[parametr]
    elif value < 350:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': "Dwutlenek siarki"}
        return dictonary[parametr]
    elif value < 500:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': "Dwutlenek siarki"}
        return dictonary[parametr]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': "Dwutlenek siarki"}
        return dictonary[parametr]

@register.filter
def o3(value, parametr):
    if value < 70:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Ozon"}
        return dictonary[parametr]
    elif value < 120:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': "Ozon"}
        return dictonary[parametr]
    elif value < 150:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': "Ozon"}
        return dictonary[parametr]
    elif value < 180:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': "Ozon"}
        return dictonary[parametr]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': "Ozon"}
        return dictonary[parametr]

@register.filter
def c6h6(value, parametr):
    if value < 5:
        dictonary = {'color': "#00cc00", 'quality': "Bardzo dobra", 'disc': "Benzen"}
        return dictonary[str(parametr)]
    elif value < 10:
        dictonary = {'color': "#00ff00", 'quality': "Dobra", 'disc': "Benzen"}
        return dictonary[str(parametr)]
    elif value < 15:
        dictonary = {'color': "#ffff99", 'quality': "Umiarkowana", 'disc': "Benzen"}
        return dictonary[str(parametr)]
    elif value < 20:
        dictonary = {'color': "#ffd633", 'quality': "Dostateczna", 'disc': "Benzen"}
        return dictonary[str(parametr)]
    else:
        dictonary = {'color': "#cc0000", 'quality': "Zła", 'disc': "Benzen"}
        return dictonary[str(parametr)]

@register.filter
def time(time):
    return str(time)

@register.simple_tag(name='my_tag')
def my_tag(key, value, parametr):
    if key =='updated':
        pass
    if key == 'pm25':
        return pm2(value, parametr)
    if key == 'pm10':
        return pm10(value, parametr)
    if key == 'no2':
        return no2(value, parametr)
    if key == 'co':
        return co(value, parametr)
    if key == 'so2':
        return so2(value, parametr)
    if key == 'o3':
        return o3(value, parametr)