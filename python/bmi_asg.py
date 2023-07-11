# Store Mark's and John's mass and height in variables
# Mark's mass in kilograms
mark_massTD1 = 78
mark_massTD2 = 95
# Mark's height in meters
mark_heightTD1 = 1.69
mark_heightTD2 = 1.88

# John's mass in kilograms
john_massTD1 = 92
john_massTD2 = 85
# John's height in meters
john_heightTD1 = 1.95
john_heightTD2 = 1.76

# Calculate both their BMIs
mark_bmiTD1 = mark_massTD1 / (mark_heightTD1 ** 2)
john_bmiTD1 = john_massTD1 / (john_heightTD1 ** 2)

mark_bmiTD2 = mark_massTD2 / (mark_heightTD2 ** 2)
john_bmiTD2 = john_massTD2 / (john_heightTD2 ** 2)

# Check if Mark has a higher BMI than John
mark_higher_bmi = mark_bmiTD1 > john_bmiTD1
mark_higher_bmi2 = mark_bmiTD2 > john_bmiTD2

# Print the results
print("Mark's BMI:", mark_bmiTD1)
print("John's BMI:", john_bmiTD1)
print("Does Mark have a higher BMI than John?", mark_higher_bmi)

print("Mark's BMI:", mark_bmiTD2)
print("John's BMI:", john_bmiTD2)
print("Does Mark have a higher BMI than John?", mark_higher_bmi2)

# who has higher BMI
if mark_higher_bmi is True:
    print("Mark's BMI " + str(mark_bmiTD1) + "is higher than John's " + str(john_bmiTD1) + "!")
else:
    print("John's BMI " + str(john_bmiTD1) + "is higher than Mark's " + str(mark_bmiTD1) + "!")

if mark_higher_bmi2 is True:
    print("Mark's BMI " + str(mark_bmiTD2) + "is higher than John's " + str(john_bmiTD2) + "!")
else:
    print("John's BMI " + str(john_bmiTD2) + "is higher than Mark's " + str(mark_bmiTD2) + "!")


# String formatting or interpolation
if mark_higher_bmi is True:
    print(f"Mark's BMI {mark_bmiTD1} is higher than John's {john_bmiTD1}!")
else:
    print(f"John's BMI {john_bmiTD1} is higher than Mark's {mark_bmiTD1}!")

if mark_higher_bmi2 is True:
    print(f"Mark's BMI {mark_bmiTD2}is higher than John's {john_bmiTD2}!")
else:
    print(f"John's BMI {john_bmiTD2} is higher than Mark's {mark_bmiTD2}!")


# # Using functions
# def mark_bmi():
#     print(mark_bmiTD1)
#     print(mark_bmiTD2)
# mark_bmi()
#
#
# def john_bmi():
#     print(john_bmiTD1)
#     print(john_bmiTD2)
# john_bmi()
#
#
# def higher_bmi():
#     if mark_higher_bmi is True:
#         print(f"Mark's BMI {mark_bmiTD1} is higher than John's {john_bmiTD1}!")
#     else:
#         print(f"John's BMI {john_bmiTD1} is higher than Mark's {mark_bmiTD1}!")
# higher_bmi()

def calculate_bmi(mass, height):
    return mass / (height ** 2)


def compare_bmi(mark_mass, mark_height, john_mass, john_height):
    mark_bmi = calculate_bmi(mark_mass, mark_height)
    john_bmi = calculate_bmi(john_mass, john_height)

    if mark_bmi > john_bmi:
        return "Mark"
    elif john_bmi > mark_bmi:
        return "John"
    else:
        return "Mark and John have the same BMI."


def print_bmi_comparison(mark_mass, mark_height, john_mass, john_height):
    mark_bmi = calculate_bmi(mark_mass, mark_height)
    john_bmi = calculate_bmi(john_mass, john_height)

    print("Mark's BMI:", mark_bmi)
    print("John's BMI:", john_bmi)

    comparison_result = compare_bmi(mark_mass, mark_height, john_mass, john_height)
    if comparison_result == "Mark":
        print("Mark has a higher BMI than John!")
    elif comparison_result == "John":
        print("John has a higher BMI than Mark!")
    else:
        print("Mark and John have the same BMI.")


# Variables for Mark and John's measurements
mark_massTD1 = 78
mark_heightTD1 = 1.69
john_massTD1 = 92
john_heightTD1 = 1.95

mark_massTD2 = 95
mark_heightTD2 = 1.88
john_massTD2 = 85
john_heightTD2 = 1.76

# Printing BMI comparisons
print("BMI Comparison for TD1:")
print_bmi_comparison(mark_massTD1, mark_heightTD1, john_massTD1, john_heightTD1)
print()

print("BMI Comparison for TD2:")
print_bmi_comparison(mark_massTD2, mark_heightTD2, john_massTD2, john_heightTD2)
