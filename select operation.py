import mysql.connector

#open database conection
db=mysql.connector.connect(user="root", password="kalharamax",host="localhost",database="Python2")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#prepare sql query to insert a record into the databases
sql="SELECT * FROM Text_1 "

#Execute the sql command
try:
    cursor.execute(sql)
    #fetch all the rows in a list of lists.
    results=cursor.fetchall()
    for row in results:

        first_name=row[0]
        last_name=row[1]
        age=row[2]
        sex=[3]
        income=[4]
        #now print fetched result
        print(first_name,last_name,age,sex,income)

except:
    print("Error:unable to fetch data")



#desconnect from server
db.close()
