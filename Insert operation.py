import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost",database="PYTHON2")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#prepare sql query to insert a record into the databases
sql="""INSERT INTO TEXT_1(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
       VALUES('Mac','monhan',20,'M',12000)"""
#Execute the sql command
try:
    cursor.execute(sql)
    #commit your changes in the database
    db.commit()
except:
    #rollback in case there is any error
    db.rollback()

#desconnect from server
db.close()
