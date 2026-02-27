#12.12 lab
#lesson 4 lab 
"""
Python Tasks: Scope, LEGB, and Basic OOP
1. Local vs Global Variable
Create a program that demonstrates the difference between a local variable and a global variable. The
program should clearly show both values.
2. Function Using a Global Variable
Write a function that reads the value of a global variable without changing it. Show in the output that the
global value remains the same after the function call.
3. Function That Modifies a Global Variable
Write a program where a function changes the value of a global variable using the global keyword.
Display the value before and after the function call.
4. Local Variable Shadowing a Global Variable
Create an example where a global variable and a local variable have the same name. The program
should demonstrate which value is used inside the function and which is used outside.
5. Inner Function and the LEGB Rule
Write a function that contains an inner function. Use print statements to show which version of a name
is being used (local, enclosing, or global).
6. Using nonlocal
Create an example where an inner function modifies a variable in the enclosing function using the
nonlocal keyword. Show the change before and after.
7. Creating Your Own Class
Write a class with at least two instance attributes and a method that prints or returns information based
on those attributes. Create at least two objects and demonstrate that they can have different values.
8. Class Attribute vs Instance Attribute
Create a program demonstrating a class attribute shared across multiple objects. Then change the
attribute for only one object and show that the other objects still use the original class attribute.
9. Class With a Calculation Method
Write a class with one attribute and a method that calculates something based on that attribute (for
example area, price, or length). Show how changing the attribute affects the calculation.
10. Method for Updating an Attribute
Write a class where an attribute can be updated through a custom method. Demonstrate how the
updated attribute changes the behavior of another method in the class.
Challenge Tasks
Challenge 1 – Tracking Variable Changes Across Scopes
Create a program that uses three nested functions. Each function should have a variable with the same
name but different values. Use print statements to show exactly which value is used at each level, and
experiment with both nonlocal and global to change the outcome.
Challenge 2 – Class With Both Class-Level and Instance-Level Behavior
Write a class that uses:
- at least one class attribute
- at least one instance attribute
- at least one method that uses the class attribute
- at least one method that uses only the instance attributes
Then add a way to change the class attribute and show how this affects all existing objects. Also show
how changing an instance attribute affects only one object.
Challenge 3 – Object Interaction
Create two different classes where objects from one class interact with objects from the other.
Demonstrate how these interactions work and how changing attributes in one object affects the result in
the other.

"""


#lesson 4 lab1
x = 20
def yep():
    x = 100
    return x

print(x) #outside of function
print(yep()) 


#lab2 
age = 20

def information(age):
    print(age) #use global age
    age = 30  
    print(age) #change global age

information(age) 
print(age)


#lab3
age = 20 

def add_age():
    global age 
    print('this function is now using global age: ', age) 
    age = 89
    print('change global age to: ', age)


print('Before calling add_age() age is : ', age) 

add_age() 
print('value of age outside of add_age() is: ', age)


#lab4
name = 'global name: M'

def show_name():
    name = 'local name: B'
    print('valuse inside the function is: ', name) 
    

print('Before calling show_name() name is: ', name)
show_name()
print('After calling show_name() name is: ',name)


#lab 5
name = 'global'

def information():
    name = 'local'  

    def new_information():
        print('enclosing ' + name)     
    new_information()

print('global name is :', name)
information() 
print('global name still is:', name)


#lab 6
def outer():
    word = 'B'
    
    def inner():
        nonlocal word
        word = 'C'
        print('enclosing word is: ', word)

    print('before calling inner() word is: ', word)

    inner()
    print('after calling inner() word is: ', word)

print('using nonlocal keyword to see changes')
outer()
print()


#lab 7
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        return (f'{self.title} Autor is: {self.author}')

Book1 = Book('Python Language', 'Alice')
Book2 = Book('Machine Learning', 'John')

print(Book1.info())
print(Book2.info())
print()


#lab 8 
class People():
    species = 'Group1'

    def __init__(self, name): 
        self.name = name

Women = People(name='Christina')
Man = People(name='Rocket')

print(f'Women name is :{Women.name}, belongs to : {Women.species}')
print(f'Man name is :{Man.name}, belongs to : {Man.species}')

People.species = 'Group2' #change Attribut
print(f'Women belongs to : {Women.species}')
print(f'Man belongs to : {Man.species}')

Women.species = "Special Group" #change instance attribute
print(f'Women belongs to : {Women.species}')
print(f'Man belongs to : {Man.species}')

#lab 9 #半径圆 半径 面积 周长
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius

circle1 = Circle(2)
circle2 = Circle(10)

print(f'radius = {circle1.radius}, area = {circle1.area():.2f}, circumference = {circle1.circumference():.2f}')
print(f'radius = {circle2.radius}, area = {circle2.area():.2f}, circumference = {circle2.circumference():.2f}')

circle1.radius = 7
print(f'radius = {circle1.radius}, area = {circle1.area():.2f}, circumference = {circle1.circumference():.2f}')


#lab 10
class BankAccount:
    def __init__(self, owner, balance = 1000):
        self.owner = owner
        self.balance = balance
    
    def withdra(self, amount):
        self.balance -= amount

account = BankAccount('Billy', 1000)
print(account.balance)

account.withdra(200)
print(account.balance)

    
#challenge 1
value = 'global'

def Nested1():
    value = 'first'

    def Nested2():
        value = 'second'

        def Nested3():
            nonlocal value
            value = 'change second value'
            print(f'Nested3 value is: {value}') # change second value
        
        print(f'before calling Nested3() value is: {value}') #second
        Nested3()
        print(f'after calling Nested3() value is: {value}') #change second value

    print(f'before calling Nested2() value is: {value}') #first
    Nested2()
    print(f'after calling Nested2() value is: {value}') #first ?

print(f'global value is: {value}') #global
Nested1()
print(f'after calling Nested1() value still is: {value}') #global












#1212 class content
#scope 范围

x = 15
def printer():
    x = 30
    return x

print(x) #15 这个print不在function/local里  所以还是x=15
print(printer()) #30  #the printer() is inside the function
print(x) #15


# 1. Name assignment will create or change local names vy default
# 2. Name references search (at most) four scopes, these are:(LEGB rule)
    # local - Name assigned in any way within a function (def or lambda) and not declared global in function
    # Enclosing functions - Name in the local scope of any and all enclosing func, inner or outer
    # Global - Names assigned at the top-level of a module file, or declared globaly in a def within a file
    # Built-in - Bult-in names, module, range.....(all that is built in)
# 3. Names declared in global and nonlocal statement map assigned names to enclosing module and function scopes

## Enclosing function
name = 'This is some global name'

def greet():
    name = 'Erik'  #有新变量值就会替代前面的值

    def hello():
        print('Hello ' + name)    #Hello Erik 
    hello()

greet() 

# Global scope
print(name) #This is some global name


##Built in function
#len()
#not using the global keywords inside the function

x = 50 #global 

def func(x):
    print('x is', x)    #50 python use the first x
    x = 2
    print('change local x to', x)  #2

func(x) #even calling func because not using global keywords

print('x is still ', x)  #50 #this is outside of the function 

x = 50

def func():
    global x 
    print('this function is now using global x') 
    print('Because of global x is : ', x) #50
    x = 2
    print('Run func(), changed global x to ', x) #2

print('Before calling func() x is :', x) #50
func() #now we call the function up will use the inside function value
print('Value of x ousdie of func() is : ', x) #2

#Before calling func() x is : 50
#this function is now using global x
#Because of global x is :  50
#Run func(), changed global x to  2
#Value of x ousdie of func() is :  2

##classes  constructor

class Sample(): #capital or not capital is same, whateve we create class XXXX() is a method
    pass #if you don't know what to write use pass means continue the code


x = Sample()

print(type(x)) #<class '__main__.Sample'>


class Dog():
    def __init__(self, breed): #this is called constructor
        self.breed = breed #breed ia a attributor 属性

milo = Dog(breed='Labrador')
frank = Dog(breed='Huskie')

print(milo.breed)
print(frank.breed)


class Dog():
    # class object atribute:
    species = 'mammal'
    def __init__(self, breed, name): #this is called constructor
        self.breed = breed #breed ia a attributor 属性
        self.name = name

milo = Dog ('Labrador', 'Milo')


print(milo.breed) #labrador
print(milo.name) #Milo
print(milo.species) #mammal

class Circle: #半径 周长 
    pi =3.14 # put a class object atribute here 放置一个类对象属性

    #Circle get instannntiated with a radius 初始化一个带有半径的圆
    def __init__(self, radius = 1):
        self.radius = radius

    #Area method claculated the area. Note the use of self!!
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    #method for resetting radius #重置半径的方法
    def setRadiu(self, radius):
        self.radius = radius 

    #Method for getting radius 获取半径的方法
    def getRadius(self): #get radius 获取半径
        return self.radius 
    
c = Circle()
c.setRadiu(2)
print('Radius is :', c.getRadius())  #2 
print('Area is: ', c.area()) #12.56

