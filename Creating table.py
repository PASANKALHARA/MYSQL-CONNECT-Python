import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost",database=" PYTHON2")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#drop table if it already exist using execute ()method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#create table as per requirement
sql="""CREATE TABLE TEXT_1(
FIRST_NAME CHAR(60)NOT NULL,
LAST_NAME CHAR(20),
AGE INT(3),
SEX CHAR(1),
INCOME FLOAT)"""

cursor.execute(sql)




#desconnect from server
db.close()

