import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#create table as per requirement
sql="""CREATE DATABASE PYTHON2"""

cursor.execute(sql)

#desconnect from server
db.close()



