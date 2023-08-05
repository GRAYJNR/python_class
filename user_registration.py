# # First import the connector
import mysql.connector

# # # Connect to mother database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user= "root",
#     password =""
# )

# myCursor = mydb.cursor()
# myCursor.execute("CREATE DATABASE registration")

# # Connect to created database
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password ="",
    database = "registration" 
)
# # Anytime you have to enter a new command you
# # first have to call on my cursor

# myCursor.execute("CREATE TABLE users(id INT PRIMARY KEY, name VARCHAR(200), email VARCHAR(200), password VARCHAR(200))")

# # INSERTing DATA INTO the user
# # Use executemany() to insert multiple rows at once
# myCursor = mydb.cursor()
# myCursor.executemany
# sql = '''INSERT INTO users (id, name, email, password) 
#          VALUES (%s, %s, %s, %s)'''

# # Inserting
# users_data = [
#     (100, "John Graham", "j.graham@gmail.com", "100@jg"),
#     (101, "Jane Graham", "ja.graham@gmail.com", "101@jag"),
#     (102, "Jesse Graham", "je.graham@gmail.com", "100@jeg")
# ]
# myCursor = mydb.cursor()
# myCursor.executemany(sql, users_data)
# mydb.commit()
# # # Creating a function to insert data
# id_data=input("enter you id number :")
# name_data= input("enter your name :")
# email_data =input("enter your email :")
# password_data = input("enter your password :")


# def create_user():
#     sql="INSERT INTO users(id, name, email, password) VALUES (%s,%s,%s,%s)"
#     val = id_data,name_data,email_data,password_data
#     print(val)
#     myCursor.execute(sql,val)

#     mydb.commit()

# create_user()

# # Encrypting a password
# id_data=input("enter you id number :")
# name_data= input("enter your name :")
# email_data =input("enter your email :")
# password_data = input("enter your password :")

 
# # First install and import bcrypt with pip
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password_data.encode(), salt)


# def create_user():
#     sql="INSERT INTO users(id, name, email, password) VALUES (%s,%s,%s,%s)"
#     val = id_data,name_data,email_data,hashed
#     myCursor.execute(sql,val)

#     mydb.commit()

# create_user()

# mycursor = mydb.cursor()
# def del_user():
#     sql = "DELETE FROM users WHERE id = %s"

# mycursor.execute(sql)

# mydb.commit()
# del_user

# class Person:
#   def __init__(self, name, email):
#     self.name = name
#     self.email = email

# p1 = Person("John", "j.graham@gmail.com")

# print(p1.name)
# print(p1.email)


mycursor = mydb.cursor()
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password ="",
    database = "registration" 
)
db_config = {
    'user': 'root',
    'password': '',
    'host': "localhost",
    'database': 'registration',
}

class LoginSystem:
    def __init__(self):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Execute SELECT query to fetch user data for the entered email
        query = "SELECT email, password FROM users WHERE email = %s;"
        self.cursor.execute(query, (email,))
        user_data = self.cursor.fetchone()

        if user_data:
            db_email, db_password = user_data
            if password == db_password:
                print("Login successful! Welcome back, {}!".format(email))
            else:
                print("Wrong credentials, try again!")
        else:
            print("Wrong credentials, try again!")

        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    login_system = LoginSystem()
    login_system.login()