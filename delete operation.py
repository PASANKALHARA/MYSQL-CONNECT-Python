import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost",database="PYTHON")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#prepare sql query to insert a record into the databases
sql="DELETE FROM EMPLOYEE WHERE AGE >20"
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
