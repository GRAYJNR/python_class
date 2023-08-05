# # Activating virtual environment
# source env/Scripts/activate


# Linkingg python to mysql
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user= "root",
    password =""
)

# print(mydb)

# # Before you create any tables you need to check if
# myCursor = mydb.cursor()
# myCursor.execute("SHOW DATABASES")

# for database in myCursor:
#     print(database)

# Creating a new database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user= "root",
#     password =""
# )
# myCursor = mydb.cursor()
# myCursor.execute("CREATE DATABASE learn_python")

# # Creating tables and columns
# mydb =mysql.connector.connect(
#     host="localhost",
#     user= "root",
#     password ="",
#     database = "learn_python"
# )
# myCursor = mydb.cursor()
# myCursor.execute("CREATE TABLE users(id INT, name VARCHAR(200))")


# INSERT DATA INTO the user
# myCursor.execute("INSERT INTO users(id,name) VALUES (1,'marley')")

# mydb.commit()


# another ways 
# sql = "INSERT INTO users(id,name) VALUES (%s,%s)"
# val = [
#     (4,'ama'),
#     (5,'nii')
# ]
# myCursor.executemany(sql,val)

# mydb.commit()

# print(myCursor.rowcount,"data was inserted ")


# # select all data from table 

# myCursor.execute("SELECT * FROM users ")

# myresult = myCursor.fetchall()

# for user in myresult:
#     print(user)



# # select a particular data from table 
# myCursor.execute("SELECT * FROM users WHERE name ='randy'")

# myresult = myCursor.fetchall()

# for user in myresult:
#     print(user)

# # Print in Ascending order
# myCursor.execute("SELECT * FROM users ORDER by ASC")

# myresult = myCursor.fetchall()

# for user in myresult:
#     print(user)