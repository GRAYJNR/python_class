# # The word "print" is used to display results in the terminal   
# print("Gray")

# name= "John Smith"
# age= 20
# status= "New Patient"


# Expression is a piece of code that produces a value

# # Using the "input" function
# name= input("What's your name? ")
# color= input("What's your favourite color? ")
# print(name + " likes " + color)


# Calculate age
# birth_year= input("Birth year: ")
# age= (2023 - int(birth_year))
# print(age)


# # Calculate weight in kg
# weightInLbs= input("What's your weight? ")
# weightInKg= int(weightInLbs) * 0.45359237
# print(weightInKg)



# # Indexes
# name = "john Graham"
# print(name[0])

# # f Formatted string
# firstname = "John"
# lastname = "Graham"
# message = firstname + " [" + lastname + "] is a coder"
# msg = f"{firstname} [{lastname}] is a coder"
# print(message)
# print(msg)


# "len" is used to find the length of data
# ".upper" is used to change a string into all caps
# ".lower" is used to change a string into all smalls
# ".title" is used to change a string's first letter into capital
# ".find" is used to identify the index number of a sequence of characters
# ".replace" is used to change letters & words in a sequence of characters
# "in" is used to locate in a sequence of characters

# course = "math"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find("t"))
# print(course.replace("m", "p"))
# print("a" in course)


# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# # "round" rounds to the nearest whole number
# x = 2.9
# print(round(x))

# # "abs" always returns a positive number
# x = -2.9
# print(abs(x))


# While loop
# # Guessing Game.
# secret_number = 9
# guess_count = 1
# guess_limit = 3
# while guess_count <= guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!')
#         break
# # break is used to end an if without an else
# else:
#     print("Sorry, You Failed!")

# # Car Game!
# command = ""
# started = False
# while True:
#     command = input(">> ").lower()
#     if command == "start":
#        if started:
#             print("Car is already started!")
#        else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#        if not started:
#             print("Car is already stopped!")
#        else:
#             started = False
#             print("Car Stopped.")
#     elif command == "help":
#        print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand the command!")


# # For loops
# # Price
# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# # Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)


# numbers = [2, 2, 2, 7, 7]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# # Print largest number
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


