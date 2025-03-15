import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost",database="python2")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#desconnect from server
db.close()
