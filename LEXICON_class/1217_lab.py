# 12.17 lab

"""
Inheritance & OOP – Exercise Set
1. Constructor Execution Order
Create a base class and two subclasses that form an inheritance chain.
Each class must print a message from its constructor.
Create an object of the most derived class and observe the order in which the
constructors are executed.
Use super() in all constructors.
2. Modifying State Through super()
Create a base class that stores a numeric value.
Create two subclasses that modify this value in di erent ways inside their
constructors.
Use super() so that each class in the inheritance chain contributes to the final value.
Print the final result.
3. Multiple Inheritance and MRO
Create two parent classes that both modify the same attribute in their constructors.
Create a child class that inherits from both parents.
Use super() in all constructors.
Print the final value and print the MRO of the child class.
Explain why the final value is produced.
4. Predict and Verify MRO
Create a diamond-shaped inheritance structure with four classes.
Before running the program, write down what you believe the MRO will be.
Then print the actual MRO and compare it with your prediction.
5. Overriding a Method and Calling the Parent
Create a base class with a method that prints a message.
Override this method in a subclass.
Inside the overridden method, call the parent version using super() and then add
additional behavior.
Call the method and show both outputs.
6. Class Variables Across Inheritance
Create a base class with a class variable.
Create two subclasses.
Override the class variable in one subclass but not the other.
Create objects from all classes and show how the value di ers depending on which
class is used.
7. Protected Attributes
Create a base class that uses a protected attribute (single underscore).
Access and modify this attribute from a subclass.
Demonstrate that the attribute can be accessed, and explain why this is allowed but
discouraged outside the class hierarchy.
8. Private Attributes and Name Mangling
Create a base class with a private attribute using double underscores.
Attempt to access the attribute directly and observe what happens.
Then access it using name mangling and explain how Python handles private
attributes internally.
9. Overriding __str__ in a Subclass
Create a base class with a meaningful __str__ method.
Override __str__ in a subclass.
Use super().__str__() inside the subclass and add subclass-specific information.
Print objects of both classes to show the di erence.
10. Design Task – Controlled Inheritance
Design a small inheritance hierarchy that models a real-world concept.
Requirements:
- Use inheritance and super() correctly
- Override at least one method
- Include at least one class variable
- Include either a protected or private attribute
- Do not use polymorphism or duck typing
Create objects and demonstrate that the inheritance structure works as intended.
"""


#12.17 lab 1

class Mom:
    def __init__(self, value):
        print(f'Mom = {value}')  #Mon = 30
        self.value = value
    
class Boy(Mom):
    def __init__(self, value):
        print(f'Boy = {value}')
        super().__init__(value)
        

class Girl(Mom):
    def __init__(self, value):
        print(f'Girl = {value}')  #Girl = 30
        super().__init__(value)

g = Girl(30)
print(g.value) #30
print(Girl.mro())


#Girl = 30
#Mom = 30
#30
#[<class '__main__.Girl'>, <class '__main__.Mom'>, <class 'object'>]


#lab2
class All:
    def __init__(self, value):
        print(f'In All = {value}')
        self.value = value

class B(All):
    def __init__(self, value):
        print(f'In B = {value}')
        super().__init__(value)
        self.value += 4

class C(All):
    def __init__(self, value):
        print(f'In C = {value}')
        super().__init__(value)
        self.value *= 2

c = C(10)
print(c.value)
print(C.mro())

#In C = 10
#In All = 10
#20
#[<class '__main__.C'>, <class '__main__.All'>, <class 'object'>]



#lab 3
class Parent1:
    def __init__(self, value):
        print(f'Parent1 = {value}')
        self.value = value 

class Parent2:
    def __init__(self, value):
        print(f'Parent2 = {value}')
        super().__init__(value)
    
class Child(Parent1, Parent2):
    def __init__(self, value):
        print(f'child = {value}')
        super().__init__(value)

c = Child(30)
print(c.value)
print(Child.mro())

#child = 30
#Parent1 = 30
#30
#[<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]


#lab 4
class A :
    def __init__(self, value):
        print(f'this is A = {value}')
        self.value = value

class B(A):
    def __init__(self, value):
        print(f'this is B = {value}')
        super().__init__(value)
    
class C(A):
    def __init__(self, value):
        print(f'this is C = {value}')
        super().__init__(value)

class D(B, C):
    def __init__(self, value):
        print(f'this is D = {value}')
        super().__init__(value)

d = D(20)
print(d.value)
print(D.mro())

#this is D = 20
#this is B = 20
#this is C = 20
#this is A = 20
#20
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


#lab 5
class Basic:
    def __init__(self, value):
        print(f'Basic is here = {value}')
        self.value = value

class Sub(Basic):
    def __init__(self, value):
        print(f'Sub is here = {value}')
        super().__init__(value)
        self.value += 5

s = Sub(30)
print(s.value)
print(Sub.mro())
#Sub is here = 30
#Basic is here = 30
#35
#[<class '__main__.Sub'>, <class '__main__.Basic'>, <class 'object'>]



#lab 6
class Variable:
    def __init__(self):
        print('Hi')

    def greeting(self):
        print("Hi Hi")

class Sub1(Variable):
    def __init__(self):
        print("Hello")
    
    def greeting(self):
        print("Hello Hello")

class Sub2(Variable):
    def __init__(self):
        print('Yes')


s2 = Sub2()
s2.greeting()
s1 = Sub1()
s1.greeting()
v1 = Variable()

#Yes
#Hi Hi
#Hello
#Hello Hello
#Hi



#lab7 
class Basic:
    def __init__(self, value):
        self._value = value   #protect #inside the class hierarchy

class Sub(Basic):
    def new(self):
        print(f'subclass can access {self._value}')
    
sub = Sub("This is Sub")
sub.new()

print(sub._value)

#subclass can access This is Sub
#This is Sub

#explain: allow is because Python think we are adult, 
#in some special situation might need to access but might cause other problems; 
#give some flexibility but might change inner result, 
#subclass might need to access to parent class inner situation but might difficult to maintain or restructure.



#lab 8
class Basic:
    def __init__(self):
        self.__private_value = 60    #private

obj = Basic()
#print(obj.__private_value) 
#AttributeError: 'Basic' object has no attribute '__private_value'. Did you mean: '_Basic__private_value'?
print(obj._Basic__private_value) #60


#lab 9
class Friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age}'

class Family(Friends):
    def __init__(self, name, age, career):
        super().__init__(name, age)
        self.career = career

    def __str__(self):
        return f'{super().__str__()}, career is {self.career}'
    
fri1 = Friends("Alice", 25)
fri2 = Friends("Bob", 30)
fam1 = Family("John", 27, "Doctor")

print(fri1)
print(fri2)
print(fam1)
        
#Alice is 25
#Bob is 30
#John is 27, career is Doctor





#lab 10

class School:
    school_name = "Sunshine"
    def __init__(self, name, age):
        self._name = name  #protect
        self.__age = age  #private
    
    def introduce(self):  #one method
        return f"I'm {self._name} my age is {self.__age}"
    
    def get_age(self):  #is private need to use get method
        return self.__age 
    
    def __str__(self):
        return f'{self.__class__.__name__}:{self._name}'


class Student(School):
    student_count = 0     #Include at least one class variable
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID #student only attribute
        Student.student_count += 1  #update student number

    def introduce(self): #Override at least one method
        return f'{super().introduce()}, my student ID is{self.studentID} '
    
    def study(self, subject):
        return f'{self._name} is study {subject}'
    
    def __str__(self):
        return f'{super().__str__()} student:{self.studentID}'
    

class Teacher(School):
    teacher_count = 0
    def __init__(self, name, age, teacherID, subject):
        super().__init__(name, age)
        self.teacherID = teacherID
        self.subject = subject
        Teacher.teacher_count += 1

    def introduce(self):
        return f'{super().introduce()}, my subject is {self.subject}, my teacherID is {self.teacherID}'
    
    def teach(self, class_name):
        return f'{self._name} is teaching {class_name}'
    
    def __str__(self):
        return f'{super().__str__()} teacher:{self.teacherID}'

student1 = Student('Bob', 16, "S001")
student2 = Student('Alice', 20, 'S002')
teacher1 = Teacher('Teacher1', 40, "T001", 'Math')
teacher2 = Teacher('Teacher2', 35, "T002", 'English')

print(f'school name is {School.school_name}')
print(f'total student number is {Student.student_count}')
print(f'total teacher number is {Teacher.teacher_count}')

print(student1.introduce())
print(student2.introduce())

print(teacher1.introduce())
print(teacher2.introduce())

print(student1.study('Math'))
print(teacher2.teach('Class7'))

print(f'student name: {student2._name}')
print(f'teacher name: {teacher1._name}')

print(f'student age: {student1.get_age()}')
print(f'teacher age: {teacher1.get_age()}')




#school name is Sunshine
#total student number is 2
#total teacher number is 2

#I'm Bob my age is 16, my student ID isS001 
#I'm Alice my age is 20, my student ID isS002 

#I'm Teacher1 my age is 40, my subject is Math, my teacherID is T001
#I'm Teacher2 my age is 35, my subject is English, my teacherID is T002

#Bob is study Math
#Teacher2 is teaching Class7

#student name: Alice
#teacher name: Teacher1

#student age: 16
#teacher age: 40
















#12.17 class content 

#inhenritance

class A:
    def __init__(self, value):
        print(f'In A.__init__ and value = {value}')
        self.value = value

class B(A):
    pass

b = B(10)
print(b.value)
#In A.__init__ and value = 10
#10


######
class A:
    def __init__(self, value):
        print(f'In A.__init__ and value = {value}')
        self.value = value

class B(A):
    def __init__(self, value):
        print(f'In B. __init__ and value = {value}')
        self.value = value

b = B(10)
print(b.value)

#In B. __init__ and value = 10
#10

#######multiples in heritence


####diamond-shaped inheritance 

class A:
    def __init__(self, value):
        print(f'In A.__init__ and value = {value}')
        self.value = value


class B(A):
    def __init__(self, value):
        print(f'In B.__init__ and value = {value}')
        super().__init__(value)
        self.value += 10


class C(A):
    def __init__ (self, value):
        print(f'In C.__init__ and value = {value}')
        super().__init__(value)
        self.value *=4
        
class D(B, C):
    def __init__(self, value):
        print(f'In D.__init__ and value = {value}')
        super().__init__(value)


d = D(10)
print(d.value) 
print(D.mro()) #see the print out order
#In D.__init__ and value = 10
#In B.__init__ and value = 10
#In C.__init__ and value = 10
#In A.__init__ and value = 10
#50
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


########
#basic class
class Animal:
    def __init__(self):
        print('Animal Created')
    
    def WhoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating...nom nom..')

# derived class
class Dog(Animal):
    def __init__(self):
        print('Dog Created')
    
    def WhoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof!')

d = Dog() #Dog Created
d.WhoAmI() #Dog
d.eat() #Eating...nom nom..  is from #class Animal
d.bark() #Woof! 




####### create an employess with all method we learn 
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)

print(emp1)
print(emp2)
#Alice Ason earns 45000
#Bob Bson earns 42000



######add developer 
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Car1', 'Cson', 50000, 'Python')

print(emp1)
print(emp2)
print(dev1)


#Alice Ason earns 45000
#Bob Bson earns 42000
#Car1 Cson earns 50000 and fav prog lang is Python



####add ppl gonna get raise salary 4% add variable for employees 
class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

#create a method to raise salary
    def increase_salary(self):
        self.salary = int(self.salary * self.increase)


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Car1', 'Cson', 50000, 'Python')

print('Before increase: ')
print(emp1)
print(emp2)
print(dev1)

emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()

print('After: ')

print(emp1)
print(emp2)
print(dev1)

#Before increase: 
#Alice Ason earns 45000
#Bob Bson earns 42000
#Car1 Cson earns 50000 and fav prog lang is Python
#After: 
#Alice Ason earns 46800
#Bob Bson earns 43680
#Car1 Cson earns 52000 and fav prog lang is Python



####special raise salary 10% (1.10)add variable for developer, other ppl increse 4% (1.04)

class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

#create a method to raise salary
    def increase_salary(self):
        self.salary = int(self.salary * self.increase)


class Developer(Employee):
    increase = 1.10
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Car1', 'Cson', 50000, 'Python')

print('Before increase: ')
print(emp1)
print(emp2)
print(dev1)

emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()

print('After: ')

print(emp1)
print(emp2)
print(dev1)

#Before increase: 
#Alice Ason earns 45000
#Bob Bson earns 42000
#Car1 Cson earns 50000 and fav prog lang is Python
#After: 
#Alice Ason earns 46800
#Bob Bson earns 43680
#Car1 Cson earns 55000 and fav prog lang is Python



##########private classes in Python
class Myclass:
    def __init__(self):
        self._internal_value = 42  #private

obj = Myclass()
print(obj._internal_value)


#######Mangling
class MyClass:
    def __init__(self):
        self.__private_value = 42  


obj = MyClass()
#print(obj.__private_value)  #this is not working
print(obj._MyClass__private_value)
#42


