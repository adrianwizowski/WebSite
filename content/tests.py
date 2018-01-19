from django.test import TestCase
from django.db import connections
import datetime

cursor = connections['db.sqlite3'].cursor()
now = datetime.datetime.now()
cursor.execute("SELECT * FROM Wrocław - Korzeniowskiego WHERE Index = %d.%d.%d, %d:00",
               [now.year, now.month, now.day, now.hour - 2])
columns = [col[0] for col in cursor.description]
print([dict(zip(columns, row)) for row in cursor.fetchall()])