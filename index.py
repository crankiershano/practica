import mariadb
import sys

conn = mariadb.connect(user="root", password="123456",host="localhost",port=3306,database="personas")

cur =conn.cursor()

cur.execute("select * from MOCK_DATA")

try:
    cur.execute("select * from MOCK_DATA")
except mariadb.Error as e:
    print(f"error:{e}")
    
conn.close()