#1219 
"""
Functional Programming, Decorators & Recursion – Exercises
Task 1: Execution-time decorator
Create a decorator that measures how long a function takes to execute.
The decorator should print the execution time after the function has finished.
Apply the decorator to a function that processes a list of numbers.
Task 2: Functional list transformation
Use a functional approach to transform a list of numbers.
Apply one operation that changes the values and one operation that filters values.
The solution must use lambda expressions together with built-in higher-order functions.
Task 3: Closure-based configuration
Create a function that returns another function.
The returned function should behave differently depending on a value captured from the
outer function.
Create at least two functions from the same factory function and demonstrate the difference
in behavior.
Task 4: Decorator that modifies return values
Create a decorator that intercepts the return value of a function.
Modify the return value in some meaningful way before returning it.
Apply the decorator to at least one function and demonstrate the effect.
Task 5: Static utility methods
Create a class that acts as a utility container.
The class should contain multiple static methods.
Each static method should perform a small, independent operation.
Demonstrate usage without creating any class instances.
Task 6: Higher-order function pipeline
Create a function that takes another function as input.
Chain multiple function calls together to process a value step by step.
Use both named functions and lambda expressions in the pipeline.
Task 7: Preserving function metadata
Create a decorator that wraps a function.
Ensure that the wrapped function retains its original metadata.
Verify this by inspecting the function’s name and documentation before and after
decoration.
Challenge Task 8: Flexible decorator with arguments
Create a decorator that accepts its own arguments.
The decorator should alter its behavior based on the provided arguments.
Apply the decorator to multiple functions using different decorator arguments.
Challenge Task 9: Recursive problem design
Design a problem that can naturally be solved using recursion.
Implement a recursive solution.
Optimize the solution using memoization.
Demonstrate the difference in performance or behavior.
Challenge Task 10: Decorators + recursion interaction
Create a recursive function that performs a calculation.
Apply a decorator that logs information about each function call.
Observe how the decorator behaves during recursive execution and explain the result.

"""

#1219 task1 Execution-time decorator
def time_decorator(func):
    def wrapper():
        print('before the function is called.')
        func()
        print('after the function is called.')
    return wrapper

@time_decorator 
def lists(): 
    print([1,2,3,4,5,6])

lists() 

#output:
#before the function is called.
#[1, 2, 3, 4, 5, 6]
#after the function is called.


#task2 Functional list transformation
#one operation to changes values  map()
#another operation to filters values filter()
#use lambda expressions
#built-in higher-order function:  map() filter()

my_list = [1,2,3,4,5,6,7,8,9,10]

changed = map(lambda num: num * 3, my_list)  #change values
filtered = filter(lambda num: num % 2 == 0, changed) #filter values

result = list(filtered)  #list transformation 

print(result) #output [6,12,18,24,30]


#task 3  Closure-based configuration 基于闭包的配置
def factory(config):    #configuration arguments 配置参数
    def inner(data):    #Closure-based 闭包函数
        return data + config #使用补获的 config
    return inner

funcA = factory(10)  #config = 10
funcB = factory(20)  #config = 20

print(f'funcA(2) = {funcA(2)}') # data = 2
print(f'funcB(3)= {funcB(3)}') #data = 3

#funcA(2) = 12
#funcB(3)= 23



#task 4 Decorator that modifies return values
def my_decorator(func):
    def wrapper(*args):
        print(f'Arguemnts passed to the function: {args}')
        result = func(*args)
        print(f'Function returned:{result}')
        return result
    return wrapper

@my_decorator #decorator the function
def add(a,b):
    return a * b

add(5, 10)

#output:
#Arguemnts passed to the function: (5, 10)
#Function returned:50


#task 5 Static utility methods

class MathContainer:
    @staticmethod      #create a static method 
    def add_numbers(x,y): #create a function here   #there is no self because @staticmethod
        return x + y 
    def multiply_numbers(x,y):
        return x * y

print(MathContainer.add_numbers(5,7))      #output: 12
print(MathContainer.multiply_numbers(5,7)) #output: 35


#task 6  Higher-order function pipeline 管道 for loop

def double(x):
    return  x * 2

def subtract(x):
    return x - 3

square_lambda = lambda x : x * x


def pipeline(value, *functions): #value 在前面 high_order function pipeline
    result = value
    for func in functions:  #loop all the functions (double/subtract)
        result = func(result)
    return result

result = pipeline(10, double, square_lambda, subtract)
print(f"pipeline result is : {result}")
#pipeline result is : 397; 10*2=20, 20*20=400, 400-3=397

result2 = pipeline(10, double, lambda x : x + 4, subtract)
print(f"mix pipeline result is :{result2}")
#mix pipeline result is :21; 10*2=20, 20+4=24, 24-3=21


#task 7 Preserving function metadata use functools

import functools

def my_decorator(func):
    @functools.wraps(func) #保留原始元数据
    def wrapper(*args, **kwargs):
        print(f'calling the below {func.__name__} function')  #this is wrapper functions
        return func(*args, **kwargs)  #now wraps the original function
    return wrapper

#now can apply decorator
@my_decorator
def say_hello(name): #original function 
    print(f'Hello my friend, {name}')

say_hello("Billy")

#calling the below say_hello function
#Hello my friend, Billy


























#1219  class content
# import  

from math import *
print(sqrt(25)) #5.0


from math import sqrt as sq  #sq means sqrt
########this is only works in module (like 1209class.py)
#Machine learning will use this a lot
print(sq(25)) #5.0
#新建一个module/文件叫my_funcs.py 在里面创建一个函数 function adder 然后再新建一个module/文件叫lex.py 把 myfunc的adder函数 import进去 然后输出


########from a math library import a sqrt function  #for the performance is better choose this one 
from math import sqrt       
print(sqrt(25)) #5.0


###########import the whole library
import math               
print(math.sqrt(25))       #i need to clarify where is the sqrt from
#5.0


##########see two difference
from math import sqrt 
import math

def sqrt(x):
    return 'hello'

print(sqrt(25))  #hello
print(math.sqrt(25)) #5.0


###########use decorator is a function to run the function, is a wraper to wrap a function
# create a simple decorator

#Message1
#function
#message2
def my_decorator(func):
    def wrapper():
        print('Something is happenning before the function is called.')
        func()
        print('Something is happenning after the function is called.')
    return wrapper

@my_decorator #is a shortcut to say -> say_hello = my_decorator(say_hello)
def say_hello(): #decorator the function  say_hello() = func()?
    print('hello')

say_hello()  # i want to call a decorated function 
#output:
#Something is happenning before the function is called.
#hello
#Something is happenning after the function is called.


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Arguemnts passed to the function: {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'Function returned:{result}')
        return result
    return wrapper

@my_decorator #decorator the function
def add(a,b):
    return a + b

add(5, 10) #call the decorator function
#Arguemnts passed to the function: (5, 10) {}
#Function returned:15


#######static methods  built in method 
class MathHelper:
    @staticmethod #create a static method 
    def add_numbers(x,y): #create a function here   #there is no self because @staticmethod
        return x + y 

print(MathHelper.add_numbers(5,7)) #12

#built in function method : 
# @staticmethod, @classmethod, @property 12.17, @abstrac method 12.18  @lambda method 12.11 
#@functools.wraps


##########@functools.wraps example:
import functools

def my_decorator(func):
    @functools.wraps(func) #Ensure that the wrapped function retains its original metadata.
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')  #this is wrapper functions
        return func(*args, **kwargs)
    return wrapper #now wraps the original function

#now can apply decorator
@my_decorator
def greet(name): #original function 
    print(f'hello,{name}')

greet("alice")

#calling greet
#hello,alice



#functional programming
#function is first class objects, function to the arguments to antoher function. this is allow us to built higher order function
##############example of higher order function

def apply_function(func, value): #is the higher-order function pipleline
    return func(value)

def square(x):  #square is func from apply_function, x is the value from apply_function
    return x * x

def cube(x): #cube is func from apply_function
    return x * x * x

#pass functions as arguments
print(apply_function(square, 3)) #9
print(apply_function(cube, 3)) #27



############lambda function example: if you only use the function once

def apply_function(func, value): #higher-order function
    return func(value)

def square(x):
    return  x * x 

square_lambda = lambda x : x * x

print(square(5)) #25
print(square_lambda(5)) #25
print(apply_function(lambda x: x + 10, 5)) #15  5 is value, so 5+10=15




########rekusrion function and memoization 自我调用函数
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5)) #120 = 5*4*3*2*1




from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):       #fibonacci  what is fibonacci?
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) #output: 55 ???
print(fibonacci.cache_info()) #output: CacheInfo(hits=8, misses=11, maxsize=None, currsize=11)


