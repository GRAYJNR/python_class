# # First import the connector
import mysql.connector

# # # Connect to mother database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user= "root",
#     password =""
# )

# myCursor = mydb.cursor()
# myCursor.execute("CREATE DATABASE phonebook")

# Connect to created database
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password ="",
    database = "phonebook" 
)

myCursor = mydb.cursor()

# myCursor.execute("""
#                  CREATE TABLE contacts 
#                  (id INTEGER PRIMARY KEY, 
#                  name TEXT NOT NULL, 
#                  phone_number TEXT NOT NULL)
#                  """)

# mydb.commit()


# Putting data into the table
id_data=input("Enter you id number :")
name_data= input("Enter your name :")
phone_number_data =input("Enter your phone_number :")


def create_contact():
    sql="INSERT INTO contacts(id, name, phone_number) VALUES (%s,%s,%s)"
    val = id_data,name_data,phone_number_data
    print(val)
    myCursor.execute(sql,val)

    mydb.commit()

create_contact()



