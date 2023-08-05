#welcome to phyton

#how to print my name
#print ('gray')

#how to write multiple lines of comments use {'''} before and after

''' this is 
multiple lines
of comment '''


#how to do calculatons
#you first have but the figures in variables
#the variables are on the left and the values on the right
#of the = sign
a = 10
b = 20
#print(a + b)

#describing the data type
alive = True
#print(type(alive))

#check data type 'type()'
#show results 'print()'

#data types
''' STRING {"" ''}
"qwerty"
FLOAT DECIMAL

INTEGER -192 TO 138394
COMPLEX NUMBER WITH LETTER J
BOOLEAN True or False '''


# mylist = ["apple" , "banana" , "cherry"]
# answer = mylist[1]
# '''print(answer[2:6])
# print(mylist[1][2:6])
# print(mylist[2])'''


# fruits = [
#     'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
#     'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
#     'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
#     'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
#     'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
#     'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
#     'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
#     'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
#     'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
#     'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
#     'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
#     'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
#     'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
#     'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
#     'watermelon', 'xigua', 'yangmei', True
# ]

#print first 20 fruits
#print(fruits[:21])

#length of items in our fruits variable
#print(len(fruits))

#check the data type of the fruits variable
#print(type(fruits))

#find thwe data type of the last element
#print(type(fruits[97]))

#change grape to africa
#fruits[3] = "Africa"
#print(fruits)

#replace first 5 fruits with 3 asteris

#fruits[0:5] = ["***","***","***","***","***"]
#print(fruits)

#"qwerty" as the 5th item
#fruits.insert(4, "qwerty")
#print(fruits)


# fruits = [
#    'apple', 'banana', 'orange', 'grape', 'strawberry']

# fruits.append("gari")
# print(fruits)

# fruits = [
#     'apple', 'banana', 'orange', 'grape', 'strawberry']
# Desserts = [
#     'apple', 'banana', 'orange', 'grape', 'strawberry']
# #fruits.extend(Desserts)
# #print(fruits)

# '''remove-using name, pop-using index, clear, del are all used to take data out'''
# fruits.remove("apple")
# print(fruits)

# fruits = ("apple", "banana", "cherry", "mango", "pineapple", "papaya")
# convert tuple to list
# newFruitlist = list(fruits)

# newfruitlist[3] = "kiwi"

# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
# tuple = (tuple1+tuple2)
# print(tuple)



# # Class
# class Human():
#     #properties
#     def __init__(self, name, color, height):
#         self.name = name
#         self.color = color
#         self.height = height

#     #method

# firstHuman = Human("gray", "red", 2.00)
# print("firstHuman:", firstHuman.name)
# print("firstHuman:", firstHuman.color)
# secHuman = Human("john", "white", 1.90)
# print("firstHuman:", secHuman.name)
# print("firstHuman:", secHuman.color)


# # File Handling
# # Opening file
# data = open("demo.txt", "rt")
# x = data.readline()
# y = data.readline()
# z = data.read()
# print(x)
# print(y)
# print(z)

# # Seeking specific lines in paragraph
# data = open('demo.txt', 'r')
# for i, line in enumerate(data, 1):
#     if i == 3:
#         print(line)
#         break

# Append 
myfile = open("demo.txt", "a")
myfile.write(">>>>>>>>>>")
myfile.close()
# ASG how to get it on a new line
myfile = open("demo.txt", "a")
myfile.write(">>>>>>>>>>\n")
myfile.close()

# # Create
myfile = open("demo.txt", "x")
myfile.write(">>>>>>>>>>")
myfile.close()

# # Write
myfile = open("demo.txt", "w")
myfile.write(">>>>>>>>>>")
myfile.close()
