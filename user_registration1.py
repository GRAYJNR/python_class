import mysql.connector

class UserManagement:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        # Create the users table if it doesn't exist
        create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                id INT PRIMARY KEY,
                                name VARCHAR(255),
                                email VARCHAR(255),
                                password VARCHAR(255))'''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_users(self, users_data):
        # Insert multiple rows into the users table
        sql = '''INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)'''
        self.cursor.executemany(sql, users_data)
        self.connection.commit()

    def login(self, email, password):
        # Check if the provided email and password match any user in the database
        sql = '''SELECT COUNT(*) FROM users WHERE email = %s AND password = %s'''
        self.cursor.execute(sql, (email, password))
        result = self.cursor.fetchone()

        if result[0] > 0:
            print("Login successful")
        else:
            print("Wrong email or password. Please try again.")

if __name__ == "__main__":
    mydb = UserManagement(host="localhost", user="your_username", password="your_password", database="your_database")

    mydb.create_table()

    users_data = [
        (100, "John Graham", "j.graham@gmail.com", "100@jg"),
        (101, "Jane Graham", "ja.graham@gmail.com", "101@jag"),
        (102, "Jesse Graham", "je.graham@gmail.com", "100@jeg")
    ]

    mydb.insert_users(users_data)

    # Test the login functionality
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    mydb.login(email, password)