from datetime import datetime
import requests
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
station_list = [8129,8128]
token = '1b444a2e8a925655a3b536eace22552dbf44058e'
for station in station_list:
    response = requests.get('http://api.waqi.info/feed/@' + str(station) + '/?token=' + token)
    data = response.json()

    result = {'ID': data['data']['idx'], 'name': data['data']['city']['name'], 'update': data['data']['time']['s'], 'pomiary': {}}
    for i in data['data']['iaqi'].keys():
        if i not in ['h', 't', 'p']:
            result['pomiary'][i] = data['data']['iaqi'][i]['v']

    try:
        stacja_sql = "INSERT INTO stacja (id, name, updated) VALUES ({}, '{}', '{}');".format(result['ID'], result['name'], datetime.strptime(result['update'], '%Y-%m-%d %H:%M:%S'))
        c.execute(stacja_sql)
        conn.commit()
    except:
        stacja_sql = "UPDATE stacja SET updated ='{}';".format(datetime.strptime(result['update'],'%Y-%m-%d %H:%M:%S'))
        c.execute(stacja_sql)
        conn.commit()

    for pomiar in result['pomiary'].keys():
        sql = "INSERT INTO pomiar (czastka, stacja, value) VALUES ('{}',{},{})".format(pomiar, result['ID'],result['pomiary'][pomiar])
        c.execute(sql)
        conn.commit()

    conn.commit()

conn.close()