from bs4 import BeautifulSoup
import requests
import re
from sortedcontainers import SortedDict
import pandas as pd
import sqlite3


def Wroc_Korz():
    r = requests.get('http://powietrze.gios.gov.pl/pjp/current/station_details/table/117/1/0')
    soup = BeautifulSoup(r.content, 'lxml')

    tables = soup.findChildren('table')

    my_table = tables[0]

    answer = {}
    rows = my_table.findChildren(['th', 'tr'])

    regex = re.compile(r'[\n\r\t]')

    for row in rows:
        row_text = []
        date = ''
        for cell in row.find_all('th'):
            if cell.text.strip():
                t = regex.sub("", cell.text)
                date = t

        for cell in row.find_all('td'):
            if cell.text.strip():
                t = regex.sub("", cell.text)
                row_text.append(t)

        answer[str(date)] = row_text

    no_keys = {k: v for k, v in answer.items() if k}
    result = {k: v for k, v in no_keys.items() if v}

    for k in result.keys():
        if len(result[k]) == 7:
            result[k][0] = {'PM10' : str(result[k][0])}
            result[k][1] = {'PM2,5' : str(result[k][1])}
            result[k][2] = {'O3' : str(result[k][2])}
            result[k][3] = {'NO2': str(result[k][3])}
            result[k][4] = {'SO2': str(result[k][4])}
            result[k][5] = {'C6H6': str(result[k][5])}
            result[k][6] = {'CO': str(result[k][6])}
        else:
            pass

    mydict = {k: v for k, v in result.items() if len(result[k]) > 6}
    result = SortedDict(mydict)

    for item in result.keys():
        list_to_dict = {}
        for i in result[item]:
            list_to_dict.update(i)
        result[item] = list_to_dict

    df = pd.DataFrame.from_dict(result, orient='index')
    df.reset_index(level=0, inplace=True)

    conn = sqlite3.connect("db.sqlite3")
    df.to_sql('Wrocław Korzeniowskiego', conn, if_exists='replace', index=False)


def Wroc_Pow():
    r = requests.get('http://powietrze.gios.gov.pl/pjp/current/station_details/table/129/1/0')
    soup = BeautifulSoup(r.content, 'lxml')

    tables = soup.findChildren('table')

    my_table = tables[0]

    answer = {}
    rows = my_table.findChildren(['th', 'tr'])

    regex = re.compile(r'[\n\r\t]')

    for row in rows:
        row_text = []
        date = ''
        for cell in row.find_all('th'):
            if cell.text.strip():
                t = regex.sub("", cell.text)
                date = t

        for cell in row.find_all('td'):
            if cell.text.strip():
                t = regex.sub("", cell.text)
                row_text.append(t)

        answer[str(date)] = row_text

    no_keys = {k: v for k, v in answer.items() if k}
    result = {k: v for k, v in no_keys.items() if v}

    for k in result.keys():
        if len(result[k]) > 2:
            result[k][0] = {'PM 2.5' : str(result[k][0])}
            result[k][1] = {'NO2' : str(result[k][1])}
            result[k][2] = {'CO' : str(result[k][2])}
        else:
            pass

    mydict = {k: v for k, v in result.items() if len(result[k]) > 2}
    result = SortedDict(mydict)

    for item in result.keys():
        list_to_dict = {}
        for i in result[item]:
            list_to_dict.update(i)
        result[item] = list_to_dict

    df = pd.DataFrame.from_dict(result, orient='index')
    df.reset_index(level=0, inplace=True)

    conn = sqlite3.connect("db.sqlite3")
    df.to_sql('Wrocław Powstańców Śląskich', conn, if_exists='replace', index=False)

Wroc_Korz()
Wroc_Pow()