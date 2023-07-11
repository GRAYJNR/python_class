# login code
login_details = [
    {
        'email': 'john@gmail.com',
        'phone_number': '1234567890',
        'username': 'john92',
        'password': 'john123'
    }
]

# Input Login details
login_input = input("Enter Email, Phone number, Username: ")

# Check if login details exist
for details in login_details:
    if (
        login_input == details['username']
        or login_input == details['email']
        or login_input == details['phone_number']
    ):
        password_input = input("Enter Password: ")
        # Correct password
        if password_input == details['password']:
            print("Login successful!")
            print("Opening 'Timeline'...")
        # Wrong password
        else:
            print("Wrong login details!")
    # Wrong login
    else:
        print("Wrong login details!")
