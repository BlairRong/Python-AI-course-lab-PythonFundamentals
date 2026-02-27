print("Blair Rong")
print('O----')
print(' ||||')
print('*' * 10)

price = 10
price = 20
print(price)

patient_name = "John Smith"
patient_age = 20
is_new = True

name = input("What is your name? ")
print("Hi " + name)

name = input("What is your name? ")
color = input("What is your favourite color? ")
print(name + " likes " + color)

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

weight = input("what is your weight in pounds? ")
kg = int(weight) * 0.45
print ("Your weight in Kg is " + str(kg))

course="Python's Course for Beginners"
course='Python for "Beginners"'
course='''
Hi John,

Here is our first email to you.

Thank you,

The support team
'''
print(course)

course = "Python for Beginners"
print(course[0])
print(course[6])
print(course[10])
print(course[ :3])
print(course[0:3])
print(course[3: ])
print(course[ : ])
print(course[0: ])
print(course[-3:-1])
print(course[1:-1])

#output=John [Smith] is a coder
first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"
#use f string is more visible
msg = f"{first} [{last}] is a coder"
print(msg)

course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.title())
print(course.find('P'))
print(course.find('O'))
print(course.find("Beginners"))
print(course.replace("Beginners", "Absolute Beginners"))
print(course.replace("P", "J"))
print("Python" in course)
print("python" in course)
print("Beginners" not in course)

print(10.1 + 3)
#get a addition result
print(10 - 3.1)
#get a subtraction result
print(11 * 3.3)
#get an integer or float result, called floor multiplication
print(10 / 3)
#get a float result, called true division
print(10 // 3)
#get an interger result, called floor division
print(10 % 3)
#get a remainder result, called modulus
print(10 ** 3)
#get 10 to the power of three result, called exponentiation

#if a<b , then a%b = a
print(2%8)
print(8%9)
print(5%10)
print(6%8)

#if a==b , then a%b =0
print(8%8)

#if a is multiple of b , then a%b =0
print(8%1)
print(4%2)
print(10%5)

#if a>b , then a%b = the remainder of a divided by b
print(14%4)
#14-4*3=2
print(10%3)
#10-3*3=1
print(14%5)
#14-5*2=4
print(20%6)
#20-6*3=2
print(9%4)
#9-4*2=1
print(13%2)
#13-2*6=1
print(14%2)
#14-2*7=0


#Augmented assignment operators
x = 10
x += 3
# x = x + 3
print(x)

x 
x -= 3
# x = x - 3
print(x)
x *= 3
#x = x * 3
print(x)
x /= 3
#x = x / 3
print(x)
x //= 3
# x = x // 3
print(x)
x %= 3 
#x = x % 3
print(x)
x **= 3
#x = x ** 3
print(x)


#operator precedence
x = 10 + 3 * 2
print(x)

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * 2 ** 2
print(x)

x = (2+3) * 10 - 3
print(x)

#math functions
x = 2.9
print(round(x))

x=-2.9
print(abs(x))

import math
print(math.ceil(2.1))

print(math.floor(2.9))

#if statement
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")


is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day") 
print("Enjoy your day")


is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day") 
print("Enjoy your day")

#price of a house is $1M if buyer has good credit 
# they need to put down 10% else they need to put down 20%
#  print the down payment
is_good_credit = True
house_price = 1000000
if is_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Down payment: ${down_payment}")



#logical operators

#and operator both need to be true
has_hign_income = True
has_good_credit = True

if has_hign_income and has_good_credit:
    print("Eligible for loan")


#or operator either one needs to be true
has_hign_income = True
has_good_credit = False

if has_hign_income or has_good_credit:
    print("Eligible for loan")

#not operator reverses the boolean value
#if applicant has good credit and does not have a criminal record
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")



#comparison operators
#if temperature is greater than 30 degrees, it's a hot day, 
# otherwise if it's less than 10, it's a cold day, 
# otherwise it's a lovely day

temperature = 31
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")


#user input their name, if name is less than 3 characters long, name must be at least 3 characters,
#otherwise if name is more than 50 characters long, name can be a maximum of 50 characters,
#otherwise, name looks good!

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")


#weight converter
#weight: 72
#(L)bs or (K)g: k
#You are 160.0 pounds

weight = input("weight: ")
unit = input("(L)bs or (K)g: ")
if unit == "l" or unit == "L":
    weight_kg = int(weight)*0.45
    print(f"You are {weight_kg} kilos")
else:
    weight_lbs = int(weight)/0.45
    print(f"You are {weight_lbs} pounds")


#or this is Mosh teacher way
weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


#while loop
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")




#guessing game while loop + if loop
#guess:1
#guess:2
#guess:3
#sorry, you failed!

#guess:9
#you win!
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input("guess: "))
    guess_count += 1
    if guess_number == secret_number:
        print("you win!")
        break
else:
    print("sorry, you failed!")



#car game code
#>help
#start-to start the car
#stop-to stop the car
#quit-to exit
#>start
#car is started...ready to go!
#>stop
#car is stopped.
#>quit
#bye

#asd
#I don't understand that!


#while condition:
#what is the condition? we want to run this loop until the user types "quit" 
command = ""
#we need to know the car is started or not, we need to store in the memory,a boolean
started = False #car is not start, is stopped

while True:
    command = input("> ").lower().strip() #move out the space on the words
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car is started...ready to go!")

    elif command == "stop":
        if not started: #is stopped
            print("car is already stopped!")
        else:
            started = False
            print("car is stopped.")

    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car 
        quit - to exit
        """)
    elif command == "quit":
        print("bye")
        break
    else:
        print("I don't understand that!")



#for loop
for item in "Python":
    print(item)

for item in ["Mosh", "John", "Sarah"]:
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)

#excerise calculate the sum of all numbers frrom list
prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price #or total += price
print(f"Total: {total}")





#nested loops  a loop inside another loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#The outer loop iterates over the range of 4 (0 to 3), and for each value of x, the inner loop iterates over the range of 3 (0 to 2).
#This results in printing all possible pairs of (x, y) coordinates where x ranges from 0 to 3 and y ranges from 0 to 2.

numbers = [5, 2, 5, 2, 2] 
for x_count in numbers:
    #print('x' * x_count) can use this way too
    output = '' #reset output for nothing
    for count in range(x_count): #now we need to add five X into this string
        output += 'x'
    print(output)



#List

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(names)
print(names[0]) #index 
print(names[-1])
print(names[1:3]) #slicing
print(names[:2])
print(names[-3:-1])

#change a name in the list
names[0] = 'ale'
print(names)

#write a program to find the lagest number in a list
numbers = [3, 5, 2, 8, 1, 4]
max_number = numbers[0] #assume the first number is the largest
for number in numbers:
    if number > max_number:
        max_number = number
print("The largest number is:", max_number)


#2D list / Matrix strong in Machine learning and Data Science

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1]=20 #change value
print(matrix[0])  #first row
print(matrix[0][1]) #first row, second column

#also can use nested loops to iterate through 2D list
for row in matrix:
    for item in row:
        print(item)




#28 list method / function
#append is to add an element to the end of the list
numbers = [3, 6, 2, 8, 4]
numbers.append(20)
print(numbers)

#insert is to add an element to a specific index of the list, like in index 2 put a number of 5
# the first argument is the index, the second argument is the value to be inserted 
numbers.insert(2, 5)
print(numbers)

#remove is to remove the first occurrence of a specific value from the list
numbers.remove(8)
print(numbers)

#clear is to remove all elements from the list
numbers.clear()
print(numbers)

#pop is to remove and return the last element of the list, or you can specify an index to remove
numbers = [3, 6, 2, 8, 4]
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)

#index is to find the index of the first occurrence of a specific value in the list
numbers = [3, 6, 2, 8, 4]
print(numbers.index(2))

#in or not in is to check if a specific value is present in the list, returns a boolean value
numbers = [3, 6, 2, 8, 4]
print(2 in numbers)
print(5 not in numbers)

#count is to count the number of occurrences of a specific value in the list
numbers = [3, 6, 2, 8, 4, 2]
print(numbers.count(2))

#sort is to sort the elements of the list in ascending order
numbers = [3, 6, 2, 8, 4]
numbers.sort()
print(numbers) #can not print(numbers.sort()) because sort() does not return anything
numbers.reverse() #if want to sort in descending order
print(numbers) 

#copy is to create a shallow copy of the list
numbers = [3, 6, 2, 8, 4]
numbers_copy = numbers.copy()
print(numbers_copy)
numbers.append(10)
print(numbers)
print(numbers_copy)

#excersice
#write a program to remove the duplicate(copy) items from a list and print the new list
numbers = [1,2,2,3,4,4,5,5,6]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)


#29 tuple similar to list but immutable, using () not []
#can't add, remove, or change elements in a tuple
numbers = [1,2,3,4] #is a list
numbers = (1,2,3,4) #is a tuple

numbers = (1,2,3)
numbers[0] = 5 #will cause an error
print(numbers[1]) #index


#30 unpacking tuple
coordinates = (1,2,3)
x,y,z = coordinates
print(x)
print(y)
print(z)

#if is a list is still working
list = [1,2,3]
x,y,z = list
print(x)
print(y)
print(z)


#31 dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets { },  and have keys and values.

#Name: John
#Email: john@gmail.com
#phone: 1234 
#key:value pairs

#define a dictionaries
customer = {
    "name": "John Smith",
    "age" : 30,
    "is_verified": True
} #define a variable as customer, valua can be anything, like string, number, boolean
print(customer["name"]) #use []to assess the value of the key
#get method is to get the value from the key

#add key value pairs
print(customer.get("birthdate", "Jan 1 1980")) #if the dictionary doesn't have this key, we supply a default value to this key

customer["tall"] = "160cm"
print(customer["tall"])

#change value
customer["name"] = "Jack Smith"
print(customer["name"])


phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = "" #now we need to add a word to an output string, so we can define a output string, we set it empty string first
for charactors in phone: #we get each charactor from phone and to access the value of the key
    output += digits_mapping.get(charactors, "!") + " " #incase ppl typle not 1234 and can get "!""
print(output)

#32 excersise emoji - dictionary split method
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",  #control+command+space to show emojis
    ":(": "😔"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)



#interview questions: recursion function 

def factorial(n):
    if n == 0:       # base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))




#33 function
def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("Start") # need to have two lines space to start another line
greet_user() #this means call the upper function
print("Finish")


#34 parameters

def greet_user(name): #add a name: parameter; name is parameter
    print(f'Hi {name}!') #or print("Hi", name) 
    print("Welcome aboard")


print("Start") # need to have two lines space to start another line
greet_user("John") #pass John here, John is an aruguments
greet_user("Marry")
print("Finish")


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start") 
greet_user("John", "Smith")  #arguments position matters
print("Finish")



#35 key word arguments, using in more math
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start") 
greet_user(last_name="Smith", first_name="John")  #arguments position matters, 
#(John, last_name=Smith) #usinge the key word argument after the position arguments.
print("Finish")

#example:
#calc_cost(total=50, shipping=5, discount=0.1)


#36 return statement
def square(number):  #calculate square of number
    return (number * number)


result = square(3)
print(result)  #or print(square(3)) is also working

#by default all the function in python return "None", you can change that, so if you have a function that calculate sth, you can return the result using return statement


#37 creating a reusable function
#reorganazi the emoji excersise code to use a function 
#we can use it in chat app or email app
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",  #control+command+space to show emojis
    ":(": "😔"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#line 2-10 should put it into a single function def

def emoji_converter(message):  #define a function
    words = message.split(" ") #line2-10 copy from top
    emojis = {
    ":)": "😊",  
    ":(": "😔"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output #we need add a return statement 


message = input(">")
result = emoji_converter(message)  #we call emoji.. to pass message and return a value
print(result)


#38 exceptions how to handle the errors in python program

age = int(input("Age: "))
print(age)

#if user input "ask" will cause valueerror


try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("invalid value") #this is when user type non numbers will appear "invalid value " instead of program crushed


try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:     #new add
    print("Age cannot be 0.")
except ValueError:
    print("invalid value")



#39 comments, using comments to explain why and how, or remind other ppl do sth


#40 classes, create new class
#use classes to define a new type, like shopping car
#we gonna create a new type called point
# point method have point.move/draw/get/distance

# we starting by definding a class key word
class Point:  # we give class a name, capital each word first word, is called Pascal naming congration,like class EmailClient
    def move(self):
        print("move")


    def draw(self):
        print("draw")


#we define a new type, so we can define new objects
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)


#41 constructors is a unction get call at the time creating the object
class Point: 
    def __init__(self, x, y):    #on the top I define a new function, init is initialise #self is a reference of current object #we call this constructor, create an object
        self.x = x
        self.y = y


    def move(self): 
        print("move")


    def draw(self):
        print("draw")



point = Point(10, 20) #self reference this object #when we creating an object - Point, we want pass value for x,y, like (10,20)
print(point.x) #whenever we talk about the point, we need to know where is the point located, to solve this problem, we use a constructor,


#excersise Person : name and talk() method
class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()

#make it more fun
class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()



#42  inheritance create a same parents

class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")


#those two lines are repeat same things

class Mammal: #so we create a new class
    def walk(self): #define a method called walk
        print("walk")

class Dog(Mammal):
    def bark(self):      # we can define a method called bark
        print("bark")

class Cat(Mammal):
    pass   #pass is tell python this is nothing 

class Flys(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()   #so we can see .walk or .bark

flys1 = Flys()
flys1.be_annoying()




#43. modules we use module to organize our code

#now we put this twp functions into a seperate module called converters, and then we can input this seperate module into any program that need converter functions
#create a new file under Python, called converters.py. select the upper code and paste into that new files.and delete the current file content

#assume now this file is empty

import converters as converters

print(converters.kg_to_lbs(70))

print(converters.lbs_to_kg(160))


#anthoer syntax input other module, instead of input the entire module, we can input specific function from that module
import converters as converters
from converters import kg_to_lbs   

kg_to_lbs(100)



#excersise, before we have find max number in the list excersise
number = [10, 3, 6, 2]
max = number[0]
for number in numbers:
    if number > max:
        max = number

print(max)
#this code have no organization, no function, no module


#write a function, call it find_max(), this function should take a list and return the largest number into the list.
#call it into a module called utils
from utils import find_maximum

numbers = [10, 3, 6, 2]
maximum = find_maximum(numbers)
print(maximum)


#44 packages - django is a container that pack the relevent module
#set a new folder/package called ecommerce or other package name
#set a new empty file called __init__.py
#set a new file called shipping.py or name.py


#因为系统找不到其他文件 所以一直报错 下面在import 前输入下面这段 就能解决
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 现在可以安全导入了
import ecommerce.shipping
ecommerce.shipping.cal_shipping()

#or from package.module, inport a specific function
from ecommerce.shipping import calc_shipping
calc_shipping()

#or import the entile module, from package to specific module, or from package.module, inport a specific function
from ecommerce import shipping
#we can access to all the functions using .operator
shipping.calc_shipping()

#test 
import ecommerce.shipping
print("成功导入！")
print("模块路径：", ecommerce.shipping.__file__) # 这会打印出shipping.py的实际路径


#45 generating random values
#search "python 3 module index" there have a lot of module can use
#mosh shows use one of the module and to generate a random value生成随机的值

import random

for i in range(3):
    print(random.random()) #random number between 0 to 1


import random

for i in range(3):
    print(random.randint(10, 20))  #we put two arguments here #random value between 10 to 20


#randomly pick an item from a list
#we have a list of teammenbers, we want to randomly pick someone as leader

import random

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)


import random   #start input a random module at the top 


class Dice:   #define a class called Dice
    def roll(self):   #a method called roll
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # don't need () python will know is a turple
    

dice = Dice() #we create an object of this dise
print(dice.roll())


#46 files and directors
#from pathlib (module) import Path (class)

from pathlib import Path

#Absolut path
# /users/desktop/pyton
# relative path


path = Path("ecommerce") #find this in path objects
print(path.exists())
#return False

path = Path("emails")
print(path.mkdir()) 
#we can create by calling mkdir make director


path = Path("emails")
print(path.rmdir()) 
#we can delete by calling rmdir remove director


from pathlib import Path

path = Path()
print(path.glob("*.py")) #* is everything, all the files *.* all the py files *.py


from pathlib import Path

#* is everything, all the files *.* all the py files *.py
path = Path()
for file in path.glob("*.py"): #glob can search files in the current path
    print(file)

from pathlib import Path

#* is everything, all the files *.* all the py files *.py
path = Path()
for file in path.glob("*"): #glob can search files in the current path
    print(file)



#47 Pypi and Pip (Huh?)
#pypi.org website have all the python packages
#can search for sms
#test engineer 
#search "openpyxl" a package to deal with excel 
#copy the word and paste it into the VS Code terminal
