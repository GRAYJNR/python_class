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

course = "math"
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("t"))
print(course.replace("m", "p"))
print("a" in course)