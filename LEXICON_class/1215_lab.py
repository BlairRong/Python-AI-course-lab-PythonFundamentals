
#12.15 lab
"""
#12.15 lab1
SECTION 1 — Pythonic Classes & Properties
1. Create a class with a property and setter. Create a class with one attribute that
can only be accessed and modified through a property and setter. Include a
method that performs a calculation using the attribute.
2. Create a class with a clean __str__ representation. Create a class with at least
three attributes and implement __str__ to make printed objects readable and
nicely formatted.
3. Create a class with a meaningful __repr__. Create a class where __repr__ returns
a string that could realistically recreate the object.
4. Create a class that initializes from **kwargs. Write a class where attributes are
automatically created from keyword arguments, even when di erent objects
receive di erent arguments.
5. Create a class that builds its string using a comprehension. Write a class whose
__str__ method constructs its output using a comprehension and join().
SECTION 2 — Dunder Methods
6. Implement __eq__. Create a class where two objects are equal if their attributes
match.
7. Implement __lt__. Create a class where objects can be compared using < based
on one chosen attribute.
8. Implement __add__. Create a class where adding two objects with + produces a
new combined object.
9. Implement __len__. Create a class where len(object) returns a meaningful
numeric value based on internal data.
10. Implement __contains__. Create a class where you can check "value in object"
using __contains__.
11. Implement __getitem__. Create a class that allows indexing with square brackets
to access internal data.
SECTION 3 — Comprehension Exercises
12. Rewrite a loop using a list comprehension. Convert any loop-based list
transformation into a single list comprehension.
13. Create a filtered list comprehension. Make a comprehension that filters elements
based on a condition.
14. Create a dictionary using a dict comprehension. Use two lists and combine them
into a dictionary via comprehension.
15. Build a formatted string using a comprehension. Generate a formatted string
from object or dictionary data using comprehension and join().
16. Create a nested comprehension. Generate a two-dimensional structure (like a
table or grid) with nested comprehensions. SECTION 4 — Combined OOP +
Scope + Pythonic Techniques
17. Demonstrate LEGB with nested functions. Create a function that contains
another function. Use variables with the same name at multiple levels and
demonstrate which is used where. Modify the enclosing variable using nonlocal.
18. Create a class that processes input using a comprehension. Write a class that
receives a list or dictionary and transforms or filters the data internally using a
comprehension.
19. Create a class that builds itself from a dictionary. Write a class that receives a
dictionary and turns every key/value pair into attributes. Build __str__ using a
comprehension.
20. Combine kwargs, property, and a dunder method. Create a class that: - accepts
all attributes via **kwargs - includes at least one property with getter and setter -
implements one or more dunder methods - includes a method that performs a
calculation using its data

"""


#12.15 Section1  #lab1

class Circle:  #算圆的周长
    pi =3.14 # put a class object atribute here 放置一个类对象属性

    #Circle get instannntiated with a radius 初始化一个带有半径的圆
    def __init__(self, radius = 1):
        self.radius = radius

    #circumference method claculated the circumference. Note the use of self!!
    @property 
    def circumference(self): 
        return 2* Circle.pi * self.radius #周长公式:C = 2*pi*r
    
    @property
    def radius_value(self):
        return self.radius
    
    @radius_value.setter
    def radius_value(self, value):
        self.radius = value
    
c = Circle()
c.radius_value = 5

print('Radius is:', c.radius_value)  
print('Circumference is:', c.circumference) 


#lab2
class Flower:
    def __init__(self, flower_name, color, meaning):    
        self.flower_name = flower_name
        self.color = color
        self.meaning = meaning
    
    def __str__(self):
        return f'{self.flower_name} is {self.color}, it represent {self.meaning}  '
    
f1 = Flower('Rose', 'available in many colors', 'sysbol of love and romance')
f2 = Flower('Tulip', 'pink, yellow and red', 'elegant and simple')

print(f1)
print(f2)


#lab3
class Information:
    def __init__(self, address, telephone):
        self.address = address
        self.telephone = telephone
        
    def __repr__(self):   
        return f'Information (address = {self.address}, telephone = {self.telephone})'

inf1 = Information('street 37','070134567')
print(inf1)    
#Information (address = street 37, telephone = 070134567)


#lab 4
class Book:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return f'The book {self.title} is writen by {self.author}.'


b1 = Book(title='Python', author = 'XXXX')
b2 = Book(title='Machine Learning', author = 'YYYYY')

print(b1)
print(b2)


#lab 5
class TV_Show:
    def __init__(self, type:dict):
        self.__dict__ = type

    def __str__(self):
        str_rep = ''
        for key, value in self.__dict__.items():
            str_rep += f'{key} = {value}, '
            return ';' .join(f' {key}: {value}' for key, value in self. __dict__.items())


type_dict1 = {
    'ZZZZ' : 'Documentary',
    'YYYYY' : 'Movie',
    'XXXX' : "Animationn"
}

type_dict2 = {
    'AAAAA' : 'Mystery',
    'BBBBB' : 'Sports show',
    'CCCCC' : "Cooking show"
}

e1 = TV_Show(type_dict1)
e2 = TV_Show(type_dict2)

print(e1)
print(e2)


#Section 2 lab6 

class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y


fruit1 = Fruit('apple', 'red')
fruit2 = Fruit('apple', 'red')

print(fruit1 == fruit2) 
#True


#lab7
class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):  
        return self.x > other.x and self.y < other.y

score1 =Score(10,20)
score2 =Score(20,10)

print(score1 > score2) 
#True


#lab 8

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b
    
num1 = Add(10, 5)

num1.__add__()

print(num1.a + num1.b) 


#lab 9 
class Numbers:
    def __init__(self, x, y, z, d):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def __len__(self):  
        return len([self.x, self.y, self.z, self.d])

numbers1 =Numbers(10,20,30,40)

numbers1.__len__()
print(len(numbers1)) 
#4


#lab 10
#Implement __contains__. Create a class where you can check "value in object" using __contains__.
class Object:
    def __init__(self, *args):
        self.values = list(args)
    
    def __contains__(self, value):
        return value in self.values

object1 = Object('cat', 'bird', 3)
print(3 in object1)
print('cat' in object1)


#lab 11
class Mylist:
    def __init__(self, *args):
        self.items = list(args) #将传入的 arguments 转成 list
    
    def __getitem__(self, index):
        return self.items[index]

list1 = Mylist(1, 2, 5, 7, 10) #不能用方括号
print(list1[2])  #5


#section 3 lab 12 
#loop
my_list = [1,2,6,4,5]
new_list = []
for item in my_list:  
     new_list.append(item)
print(new_list)

#list comprehension
my_list = [1,2,6,4,5]
new_list = [item for item in my_list]
print(new_list)


#lab13
numbers = [3, 6, 7, 9, 2, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
#[6, 2, 6]


#lab14 
#Create a dictionary using a dict comprehension. Use two lists and combine them into a dictionary via comprehension.
keys = ['name','age', 'city']
values = ['John', 25, 'USA']
person = {keys[word]:values[word] for word in range(len(keys))}
print(person)
#{'name': 'John', 'age': 25, 'city': 'USA'}


#lab15 
#Build a formatted string using a comprehension. Generate a formatted string from object or dictionary data using comprehension and join().
#from a dictionary
person = {
    'name' : 'Bob',
    'age' : 20,
    'city' : "China",
    'Job': 'IT'
}

formatted_str = '\n'.join([f'{key}:{value}'for key, value in person.items()])      #'\n' 是告诉 python这是新一行

print(formatted_str)
# name:Bob
# age:20
# city:China
# Job:IT


#from object
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student('John', '65'),
    Student('Billy', '80'),
    Student('Alcie', '90')
]

student_info = ' | '.join([f'{s.name}: {s.score}'for s in students])
print(student_info)
#John: 65 | Billy: 80 | Alcie: 90


#lab 16. Create a nested comprehension. Generate a two-dimensional structure (like a table or grid) with nested comprehensions. 
matrix = [[[i + j for j in range (3)]]for i in range (3)]
print(matrix)
#[[[0, 1, 2]], [[1, 2, 3]], [[2, 3, 4]]]


#SECTION 4 — Combined OOP + Scope + Pythonic Techniques
#lab 17            #12.12上课内容
#Demonstrate LEGB with nested functions. Create a function that contains another function. Use variables with the same name at multiple levels and demonstrate which is used where. Modify the enclosing variable using nonlocal.
def outer():
    word = 'B'
    
    def inner():
        nonlocal word
        word = 'C'
        print('enclosing word is: ', word)

    print('before calling inner() word is: ', word)

    inner()
    print('after calling inner() word is: ', word)

outer()
print()


#lab18  #12.15 上课内容 ???
class Filter_list:
    def __init__(self, data):
        self.original_data = data
        self.filtered_data = None


    def filter_even(self):
        self.filtered_data = [x for x in self.original_data if x % 2 == 0 ]
        return self
    

    def get_result(self):
        return self.filtered_data
    
numbers = [1, 4, 5, 6, 8, 9]
filter_obj = Filter_list(numbers)
result = filter_obj.filter_even().get_result()
print(f'even is :{result}')
#even is [4,6,8]



#lab 19 
#Create a class that builds itself from a dictionary. Write a class that receives a dictionary and turns every key/value pair into attributes. Build __str__ using a comprehension.
class Dict_To_Object:
    def __init__(self, data_dict):
        for key, value in data_dict.items():
            setattr(self, key, value) #把字典里的每个简直对转换为属性 change into attributes
    
    def __str__(self):
        return ', '.join(f'{key} = {value}' for key, value in self.__dict__.items())

data_dict1 = {
    'a' : 10,
    'b' : 20,
    'name' : "One"
}

d1 = Dict_To_Object(data_dict1)

print(d1)
#a = 10, b = 20, name = One


#lab 20
#Combine kwargs, property实现计算属性, and a dunder (__str__)或其他 method. Create a class that: - accepts all attributes via **kwargs - includes at least one property with getter and setter验证数据类型 - implements one or more dunder methods - includes a method that performs a calculation using its data

class Combination:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # accepts all attributes via **kwargs

    @property  #实现计算属性
    def value(self):
        if hasattr(self, '_value'):  #getter implements 计算总和
            return self.value
        return sum (value for key, value in self.__dict__.items() if isinstance(value,(int, float)))
    
    @value.setter
    def value(self, new_value):      #属性setter 设置并验证 
        if not isinstance(new_value,(int, float)):
            raise ValueError('value need to be number')
        self._value = new_value

    def __str__(self):  #dunder method
        attrs = ", ".join(f'{key}={value}' for key, value in self.__dict__.items())
        return f"Combination({attrs})"
    
    def calculate(self):
        numbers = [value for key, value in self.__dict__.items() if isinstance(value, (int, float))]
        return sum(numbers) / len(numbers) if numbers else 0
    
combination = Combination(x=10, y=20, z=30, name='test')
print(combination)
print('sum:', combination.value)
print('average value:', combination.calculate())    

#Combination(x=10, y=20, z=30, name=test)
#sum: 60
#average value: 20.0
















#1215  class content

# class - property more readble
#radius 半径
#area 面积      S = pi*r**2
#circle 圆  
#circumference 周长公式:C = 2*pi*r

class Circle:
    pi =3.14 # put a class object atribute here 放置一个类对象属性

    #Circle get instannntiated with a radius 初始化一个带有半径的圆
    def __init__(self, radius = 1):
        self.radius = radius

    #Area method claculated the area. Note the use of self!!
    @property
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    @property #属性
    def radius_value(self):
        return self.radius
    
    @radius_value.setter
    def radius_value(self, value):
        self.radius = value
    
c = Circle()
c.radius_value = 2

print('Rasiua is:', c.radius_value)
print('Area is:', c.area)



class Person:
    def __init__(self, name, email, age): #three attributes
        self.name = name
        self.email = email
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and has email {self.email} '
    
p1 = Person('Alice', 'alice@gmail.com', 34)
p2 = Person('Bob', 'bob@gmail.com', 35)

print(p1)
print(p2)

p1.phone = '07213123'
print(p1.phone)



#dictionary
#args number any int
#kwargs  name/age any str

class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


p1 = Person(name='Alice', age = 23)
p2 = Person(name='Bob', age = 45)

print(p1)
print(p2)



class Something:
    def __init__(self, data:dict):
        self.__dict__ = data

    def __str__(self):
        str_rep = ''
        for key, value in self.__dict__.items():
            str_rep += f'{key} = {value}, '
            #can use comprehension inheritance 把上面的换成另一种方式 
            return ',' .join(f' {key}, {value}' for key, value in self. __dict__.items())


data_dict1 = {
    'a' : 10,
    'b' : 20,
    'name' : "One"
}

data_dict2 = {
    'a' : 15,
    'b' : 25,
    'name' : "Two"
}

s1 = Something(data_dict1)
s2 = Something(data_dict2)

print(s1)
print(s2)


#创建在 x y 坐标上的两个点

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(10, 20) 

print(point1.x, point1.y) #10 20 



#if we want to create sentence use built in function
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):   #repr more to developer 
        return f'Point(x = {self.x}, y = {self.y})'

point1 = Point(10, 20)
print(point1)    #Point(x = 10, y = 20)


#same thing
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x = {self.x}, y = {self.y})'
    
    def __str__(self):  #str more to user
        return f'Point object with (x = {self.x}, y = {self.y})'
    

point1 = Point(10, 20) 
print(point1) #Point object with (x = 10, y = 20)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(10, 20)
point2 = Point(10, 20)

print(point1 == point2) #False



#if we want to compare this two we use eq 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other): #eq equal
        return self.x == other.x and self.y == other.y
    
    #def __ne__(self, value):
        #return self.x == value.x and self.y == value.y


point1 = Point(10, 20)
point2 = Point(10, 20)

print(point1 == point2) #True


#if you want to swarp two number position use swap method 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap_xy(self):  #swarp
        self.x, self.y =self.y, self.x

point1 =Point(10,20)

point1.swap_xy()
print(point1.x, point1.y) #20 10

