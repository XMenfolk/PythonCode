# coding=utf-8
import mysql.connector
import sys
try:
    conn = mysql.connector.connect(host='192.168.217.130',
                                   port=3306,
                                   user='admin',
                                   password='admin',
                                   db='showslow',
                                   use_unicode='True')
except Exception, e:
    print e
    sys.exit()

cursor = conn.cursor()
sql = 'select * from dynatrace where id=22'


try:

    a = cursor.execute(sql)
    values = cursor.fetchall()
    print values

except Exception, e:
    print e