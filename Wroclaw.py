import requests
import sqlite3

def wroc_pow():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    token = '1b444a2e8a925655a3b536eace22552dbf44058e'
    response = requests.get('http://api.waqi.info/feed/@8129/?token=' + token)
    data = response.json()
    result = {'ID': data['data']['idx'], 'name': data['data']['city']['name'],
              'data': {'Date': data['data']['time']['s'], 'PM 2.5': data['data']['iaqi']['pm25']['v'],
                       'NO2': data['data']['iaqi']['no2']['v'], 'CO': data['data']['iaqi']['co']['v']}}

    for i in result['data'].keys():
        sql = "UPDATE Data_air SET '{}' = ? WHERE ID = ?".format(i)
        c.execute(sql, (result['data'][i], result['ID'],))

    conn.commit()
    conn.close()


def wroc_korz():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    token = '1b444a2e8a925655a3b536eace22552dbf44058e'
    response = requests.get('http://api.waqi.info/feed/@8128/?token=' + token)
    data = response.json()
    result = {'ID': data['data']['idx'], 'name': data['data']['city']['name'],
              'data': {'Date': data['data']['time']['s'], 'PM 2.5': data['data']['iaqi']['pm25']['v'],
                       'PM 10': data['data']['iaqi']['pm10']['v'], 'O3': data['data']['iaqi']['o3']['v'],
                       'NO2': data['data']['iaqi']['no2']['v'],
                       'SO2': data['data']['iaqi']['so2']['v'], 'CO': data['data']['iaqi']['co']['v']}}

    for i in result['data'].keys():
        sql = "UPDATE Data_air SET '{}' = ? WHERE ID = ?".format(i)
        c.execute(sql, (result['data'][i], result['ID'],))

    conn.commit()
    conn.close()


wroc_pow()
wroc_korz()

'''''''''
import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

token = '1b444a2e8a925655a3b536eace22552dbf44058e'
response = requests.get('http://api.waqi.info/feed/@8128/?token=' + token)
data = response.json()
result = {'ID': data['data']['idx'], 'name': data['data']['city']['name'],
          'data': {'Date': data['data']['time']['s'], 'PM 2.5': data['data']['iaqi']['pm25']['v'],
                   'PM 10': data['data']['iaqi']['pm10']['v'], 'O3': data['data']['iaqi']['o3']['v'],
                   'NO2': data['data']['iaqi']['no2']['v'],
                   'SO2': data['data']['iaqi']['so2']['v'], 'CO': data['data']['iaqi']['co']['v']}}

# c.execute("INSERT INTO Cities VALUES (?,?)", (result['ID'],result['name'],))
for i in result['data'].keys():
    sql = "UPDATE Data SET '{}' = ? WHERE ID = ?".format(i)
    c.execute(sql, (result['data'][i], result['ID'],))

conn.commit()
conn.close()
'''''