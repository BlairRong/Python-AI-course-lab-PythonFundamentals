

#1211 lab

"""
LAB 1 — Range & Loops (Numbers and Iteration)
Create a program that:
1. Prints all odd numbers from 1–20
2. Calculates and prints the sum of numbers from 1–100
3. Asks the user for a number and prints its multiplication table (1–10)
Goal: Practice range(), loops, and numeric iteration.

LAB 2 — Lists & Comprehensions
Create a program that:
1. Takes a given list of numbers
2. Generates and prints:
o A list of squares using a loop
o A list of squares using a list comprehension
o A list of positive numbers using a comprehension
Goal: Practice list operations, loops, and list comprehensions.

LAB 3 — Functions & Conditionals
Create functions that:
1. 2. 3. 4. Return a greeting with a name
Return a default greeting if no name is given
Check if a number is even
Add two numbers only if both are even, otherwise return 0
Goal: Practice function creation, return values, and conditional logic.

LAB 4 — Filter & Lambda Functions
Create programs that:
1. 2. 3. 4. Use filter() + a function to keep only even numbers
Use filter() + lambda to keep only even numbers
Filter names that have 3 or more characters
Filter words that contain the letter "a"
Goal: Practice the filter() function and lambda expressions.

**LAB 5 — *args and kwargs
Create functions that:
1. 2. 3. 4. Accept any number of values using *args and return their sum
Accept any number of values using *args and return the maximum
Accept any number of keyword arguments using **kwargs and print them
Combine a, *args, and **kwargs and print all arguments in a readable way
Goal: Practice flexible function parameters and argument unpacking.

LAB 6 — Even Number Filter Tool (Mini Project)
Create a program that:
1. Accepts a line of numbers from the user
2. Converts the input into a list of integers
3. Uses filter() + lambda to keep only even numbers
4. Prints:
o The list of even numbers
o The count of even numbers
Goal: Practice input handling, list processing, and the filter() function.

"""


#Lesson 3 Lab 1
#1.1
for i in range(20):
    if i % 2 != 0:
        odd_numbers = i
        print(odd_numbers)

#or
for i in range(1,21,2):
    print(i)

#2.1
number = 1
for i in range(100):
    number += i
print(number)

#3.1
number =int(input('please input a number from 1 to 10: '))
for i in range(1,11):
    multiplication_table_result = number * i
    print(f'{number} * {i} = {multiplication_table_result}')

    
#lesson3 lab 2
#2.1 #squares 平方数
numbers = [1,2,3]
for i in numbers:
    squares = i ** 2
    print(squares)

#2.2
numbers = [1,2,3]
squares = [i ** 2 for i in range(1,4)]
print(squares)

#2.3
numbers = [1,-2,3,-4]
positive_numbers = [i for i in numbers if i >= 0]
print(positive_numbers)


#lesson 3 lab3
#3.1
def greet_user(name):
    print(f"Hi {name}")

greet_user("Blair")

#3.2 #default greeting 默认问候语
def greet_user(name):
    if {name} : False
    print(f"Hi there")

greet_user("")

#3.3
def even_number(number):
    if number % 2 == 0:
        print(f'{number} is even number')
    else:
        print(f'Is not even number')

even_number(6)


#3.4
def addEvenOnly(num1, num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        return num1 + num2
    else:
        return 0

result1 = addEvenOnly(2,2)
result2 = addEvenOnly(3,4)
result3 = addEvenOnly(5,7)

print(result1)
print(result2)
print(result3) 



#lesson 3 lab4
#4.1
numbers = [1,2,3,4,5,6]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, numbers) 

print(list(result))

#4.2
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda i: i % 2 == 0, numbers))
print(even_numbers)

#4.3
names = ["Bob", "Alice", "John", "AI"]
long_names = list(filter(lambda name: len(name) >= 3, names))
print(long_names)

#4.4
words = ["apple", "food", "pear", "juice"]
contain_a_words = list(filter(lambda words: 'a' in words, words))
print(contain_a_words)


#lesson 3 lab 5
#5.1

def numbers(*args):
    return sum(args)

result = numbers(2,5)

print(result)

#5.2
def numbers(*args):
    return max(args)

result = numbers(3, 6, 10)

print(result)

#5.3 #dictionary

def keyword(**kwargs):
    print(f'kwargs = {kwargs}')

keyword(name='Billy', age=20, email='Billy@email.com')

#5.4
def combine (a, *args, **kwargs):
    print(f'a = {a}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')

combine(1, 2, high = 160)

#lab 6  split() list comprehensive

str_numbers =input("plese input a line of numbers by spaces: ")
list_numbers = [int(i) for i in str_numbers.split()]
even_numbers = list(filter(lambda i: i % 2 == 0, list_numbers))

print(even_numbers)
print(len(even_numbers))










#1211  class content
#for loop
nums = list(range(5))
print(nums)

x = [1,2,3]
out = []
for item in x:
    out.append(item**2)
print(out)
#or
print ([item**2 for item in x]) #is the same result as upp


#function thinking of programm design
#len()
#built function
#create function:

def my_func(param1 = 'default'):
    '''
    Docstring for my_func  
    
    :param param1: Description
    '''
    print(param1)

def hello():
    print('hello')

hello()


def giveMeHello():
    return "hello"

result = giveMeHello() #we need to assign to another variable
print(result)

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))

    print(num %2 == 0)

evenCheck(42)

def helloYou(name="Default name"):
    return('Hello,'+name)

result = helloYou('Haithem')
print(result)


def addEvenOnly(num1, num2):
    '''
    Docstring for addEvenOnly
    
    :param num1: Description
    :param num2: Description
    '''
    '''
    Imput: Two numbers
    OUTPUT: False if one numbers are not even,
    the sum if one numbers are even
    '''
    if (num1 % 2!=0) or (num2 % 2 != 0):
        return False
    else:
        return num1+num2

y = addEvenOnly(1,2)
x = addEvenOnly(2,2)

print(y)
print(x)


def timeTwo(num):
    return num * 2
print(2)

#or
lambda num: num * 2 #if you only use function once


my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2 == 0

evens = filter(evenBool,my_list)
#print(list(evens))

#or 下面这个和上面是同个意思
evens = filter(lambda num: num%2 == 0, my_list)
print(list(evens))

#this is built method
st = 'hello my name is blair'
st.lower() #this is a method
st.upper() 
st.split()

d = {'k1':1, 'k2':2}
d.key() 
d.items() #this is show all the elements not method

list.pop()

def func(a, b, c =10, d=11):


def func(*args): #args is positional arguments, output is tuple
    print(args)

func()
func(1)
func(1,2)
func(1,2,3)

def func2(a,b, **kwargs):  #key words argument
    print(a,b)
    print(kwargs) #kwargs is print out a dictionary

func2(1,2,c=12,d=17)


#make some input flexible
def func3 (a,b, *args, name ="blair", **kwargs):
    print('a= {}'.format(a))
    print('b= {}'.format(b))
    print('args = {}'.format(args))
    print('name ={}'.format(name))
    print('kwargs = {}'.format(kwargs))

func3(1,2)

#output
a= 1
b= 2
args = ()
name =blair
kwargs = {}

func3(1,2,3,name='Anna', age=35, email='blair@email.com')
#output
a= 1
b= 2
args = (3,)
name =Anna
kwargs = {'age': 35, 'email': 'blair@email.com'}

number = [1,2,3,4,5,6]

def is_even(num):
    return num%2 == 0

result = filter(is_even, number) #built funtion base on some condition

print(list(result))



