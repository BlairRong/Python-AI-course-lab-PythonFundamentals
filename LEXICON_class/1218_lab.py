#12.18 lab
"""
LAB 1 — Discover Duck Typing
Objective
Understand that shared behavior, not shared type, enables polymorphism.
Instructions
1. Write a function that:
o accepts a single argument
o calls one method on that argument
2. Call the function with:
o a built-in type
o a custom class you create yourself
3. The function must work without modification for both.
Constraints
• Do NOT use isinstance
• Do NOT check types explicitly
LAB 2 — Break Duck Typing on Purpose
Objective
Understand the risk of duck typing.
Instructions
1. Take your function from Lab 1.
2. Pass an object that does not implement the expected behavior.
3. Observe the error.
4. Explain:
o when the error occurs
LAB 3 — EAFP vs LBYL
Objective
Practice EAFP-style error handling.
Instructions
1. Write a function that:
o performs an operation on two inputs
o may fail depending on the inputs
2. Implement it using:
o try
o except
3. Test the function with:
o valid inputs
o invalid inputs
o edge cases
Constraints
• Do NOT use isinstance
• Do NOT pre-check types
LAB 4 — Build Polymorphism with Inheritance
Objective
Understand method overriding and runtime dispatch.
Instructions
1. Design a base class representing a general concept.
2. The base class must define a method but not implement it.
3. Create at least three subclasses that:
o inherit from the base class
o override the method with different behavior
4. Write a function that:
o accepts the base class
o calls the method
o does NOT use conditionals
5. Call the function with each subclass.
Constraints
• Do NOT use if, elif, or isinstance
LAB 5 — Feel the Pain of isinstance
Objective
Recognize why type-check chains do not scale.
Instructions
1. Write a function that:
2. 3. 4. o accepts an object
o behaves differently depending on the object’s type
o uses isinstance
Add a new class that should be supported.
Identify all places that must be modified.
Redesign the solution using polymorphism so:
o new classes require no changes to existing functions
LAB 6 — Abstract Base Class Enforcement
Objective
Understand why ABCs exist.
Instructions
1. Design an abstract base class that:
o represents a role or capability
o defines at least one abstract method
2. Attempt to:
o create a subclass that does not implement the method
o instantiate it
3. Observe and explain the error.
4. Create:
o one valid subclass
o a second valid subclass with different behavior
5. Write a function that:
o accepts the abstract base class
o calls the abstract method
LAB 7 — Duck Typing vs ABCs (Comparison Lab)
Objective
Compare flexibility vs safety.
Instructions
1. Solve the same problem twice:
o once using duck typing
o once using an abstract base class
2. Intentionally violate the expected interface in both versions.
3. Compare:
o error timing
o error messages
o developer experience

"""

#1218 lab1  Discover Duck Typing

def make_it_upper(d): #accepts a single argument
    return d.upper()  #calls one method 

class Crazy:
    def __init__(self, word):
        self.word = word
    
    def upper(self):
        return self.word.upper() + "~~~~~~~"
    
print(make_it_upper('yes')) #a built-in type str
print(make_it_upper(Crazy('yes')))  #a custom class crazy
#YES
#YES~~~~~~~


#lab 2 Break Duck Typing on Purpose
def make_it_upper(d): 
    return d.upper()  #upper implement

class Crazy:
    def __init__(self, word):
        self.word = word
    
    def upper(self):
        return self.word.upper() + "~~~~~~~"

print('before pass:')
print(make_it_upper('yes'))
print(make_it_upper(Crazy('yes')))

#Pass an object that does not implement the expected behavior.
print('after pass an obj without upper() like int')
print(make_it_upper(12345))

#Traceback (most recent call last):
#  File "/Users/ron/Desktop/pyhton/code储存代码/LEXICON_class/1211_lab.py", line 1310, in <module>
#    print(make_it_upper(12345))
#          ~~~~~~~~~~~~~^^^^^^^
#  File "/Users/ron/Desktop/pyhton/code储存代码/LEXICON_class/1211_lab.py", line 1295, in make_it_upper
#    return d.upper()  #upper implement
#           ^^^^^^^
#AttributeError: 'int' object has no attribute 'upper'

#explain: the error happend in runtime not at the compile time, it happends when it in "make_it_upper()try to use d.upper()"


#lab 3 EAFP
def safe_add(c,d):
    try:
        result = c / d
        return f'rerult is {result}'
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero'
    except TypeError as e:
        return f"Error: Invalid types = {e}"
    
print(safe_add(2,3))
print(safe_add(10,0))
print(safe_add(0, 5))

#rerult is 0.6666666666666666
#Error: Cannot divide by zero
#rerult is 0.0


#lab 4  Build Polymorphism with Inheritance
class School:
    def name(self):
        raise NotImplementedError   #The base class must define a method but not implement it.

class Teacher(School):
    def name(self):                   #override the method with different behavior
        return "Hi, I'm Teacher"

class Student(School):
    def name(self):
        return "Hello, I'm Student"

class Other_Staff(School):
    def name(self):
        return "I'm staff"
    
print(Teacher().name()) 
print(Student().name()) 
print(Other_Staff().name())

#Hi, I'm Teacher
#Hello, I'm Student
#I'm staff


#lab 5 Feel the Pain of isinstance
def sound(animal):
    if isinstance(animal, Dog): #behaves differently depending on the object’s type
        return "Woof!" 
    elif isinstance(animal, Cat):
        return "Meow~"
    else:
        return "Unknown animal"
    
class Dog:
    pass

class Cat:
    pass

print(sound(Dog())) #Woof!
print(sound(Cat())) #Meow~

#add new class
class Bird:
    pass

def sound(animal):
    if isinstance(animal, Dog): 
        return "Woof!" 
    elif isinstance(animal, Cat):
        return "Meow~"
    elif isinstance(animal, Bird):
        return "JiJi"
    else:
        return "Unknown animal"
    
print(sound(Bird())) #JiJi


#redesign use polymorphism:
class Animal:
    def sound(self):
        raise NotImplementedError  

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return 'Meow~'

print(Dog().sound()) #Woof!
print(Cat().sound()) #Meow~

class Bird(Animal):
    def sound(self):
        return "JiJi"

print(Bird().sound()) #JiJi


#lab 6  Abstract Base Class Enforcement
from abc import ABC, abstractmethod 

class Role(ABC):         #represents a role
    @abstractmethod 
    def introduce(self, obj):  #abstract method
        pass

class BadEmployee(Role):  #create a subclass that does not implement the method
    pass

#bad_employee = BadEmployee()
#print(bad_employee) ##???

class CEO(Role):
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        return f"{self.name} is the CEO"

class Manager(Role):
    def __init__(self,name):
        self.name = name

    def introduce(self):
        return f"{self.name} is the Manager"

def role_inntroduction(person):    #write a function accepts abstract base class and call the method
    return person.introduce()

ceo = CEO("Billy")
manager = Manager("Jacob")

print(role_inntroduction(ceo))
print(role_inntroduction(manager))
#Billy is the CEO
#Jacob is the Manager


#lab 7 

#duck typing : Flexibility
def make_quack(animal):
    return animal.quack() #call method without checking types

class Duck:
    def quack(self):
        return "Quack!"

class Bird:
    def Ji(self):
        return "JiJi"

duck = Duck()
print(make_quack(duck)) #Quack!

bird = Bird()
print(make_quack(bird)) 
#error timing: when is runtime call the method,
#developer experience: only when is running then will find the problems


#ABCs : Safety
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def quack(self):
        pass

def make_quack(animal):
    return animal.quack()

class Duck(Animal):
    def quack(self):
        return "Quack!"
    
class Bird(Animal):
    def Ji(self):
        return "JiJi"
    
duck = Duck()
print(make_quack(duck)) #Quack!

try:
    bird = Bird() #find the error here
except TypeError as e:
    print("error")

#experience : more earlier find error, more safety


























#1218 class content

#poly  = many
#morph = form

#polumorphism
#same peice of code can work with different kind objects
#i can write only one and can work on many object i give

#without polymorphism 
#if
#elif
#isinstance

#with polymorphism
#code is shorter
#code is easier to extend
#code breaks less when we add nenw feauters


#Duck typing example 1

def make_it_upper(s):
    return s.upper() #we assume s have a method called upper, so this is polymorphism

class Shouty:
    def __init__(self, text):
        self.text = text
    
    def upper(self):
        return self.text.upper() + "!!!"
    
print(make_it_upper('hello'))
print(make_it_upper(Shouty('hello'))) 
#####same function but two different objects types, same method called two different behavior, this is polymorphism duck typing
#HELLO
#HELLO!!!

# two defense programming  LBYL & EAFP
#one is look before you leep (LBYL)
#if  isinstance(x, str):
#    print(x.upper())

#another one is easier to ask forgiveness than permission (EAFP)
#this is safe way to do 
def safe_upper(x):
    try:
        return x.upper()
    except AttributeError:
        return str(x).upper()
    
print(safe_upper("hi"))
print(safe_upper(123))
print(safe_upper(Shouty('hi')))

#HELLO
#HELLO!!!
#HI
#123
#HI!!!



#polymorphism with inherentens example 

#we define a base class
#we define subclasses
#subclasses override methods

class Animal:
    def speak(self):
        raise NotImplementedError  #is a rule not a implementation all the animal need to speak

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return 'meow'

print(Dog().speak()) #Woof!
print(Cat().speak()) #meow

#this is called subtype polymorphism
#they have same method but different output


#this is polyphysom with abstractmethod
####abstract base class

#is can not be initiated usefully on its own, it defins methods, that must be basically implement by subclass, and acts like contracts between basic class and its sub class
#so abstract is basically answer one questions, what method must exit for this object to be considered valid,

#start with an import here:

from abc import ABC, abstractmethod  #abstract is a decurator
import json

class Serializer(ABC):
    @abstractmethod 
    def serialize(self, obj): 
        pass

class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj)

js = JsonSerializer()
print(js.serialize({"name":'Billy'})) #{"name": "Billy"}

#we have same method same interface but we have different behavior
class SimpleCsvSerializer(Serializer):
    def serialize(self, obj):
        keys = obj[0].keys()
        lines = [','.join(keys)]
        for row in obj: 
            lines.append(','.join(str(row[k]) for k in keys))
        return "\n".join(lines)

csv = SimpleCsvSerializer()
print(csv.serialize([
    {"name" : "Alice", "age": 30},
    {"name" : "Emma", "age": 25}
]))

#{"name": "Billy"}
#name,age
#Alice,30
#Emma,25



