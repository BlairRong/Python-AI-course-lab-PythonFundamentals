
#1210 Lab
"""
1. String Indexing
Given the string s = 'Python', use indexing to print the following:
- 'o'
- 'Pyth'
- 'yth'
- 'nohtyP'
2. Nested List
Given the list l = [3, 7, [1, 4, 'hello']], change the value 'hello' to 'goodbye'.
3. Dictionaries – Access Values
Using keys and indexing, retrieve the value 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
4. Sets – Unique Values
Use a set to find the unique values in the list:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
5. Print Formatting
You are given the variables:
age = 4
name = 'Sammy'
Use print formatting to display:
"Hello my dog's name is Sammy and he is 4 years old"
6. Loop – Power Calculation
Write a program that takes two integers as input (base and exponent) and calculates the
power using loops.
7. Tuple – Sum of Elements
Write a program that calculates the sum of all elements in a given tuple.
8. Tuple with Condition
Create a new tuple that contains only the even numbers from a given tuple of integers.
9. Dictionaries – Merge
Write a program that merges two dictionaries into one. If a key exists in both, the value from
the second dictionary should be used.
10. List Comprehension – Even Numbers
Write a program that takes a list of integers and uses list comprehension to create a new list
containing only the even numbers.
11. String – Reverse
Write a program that takes a string as input and prints the reversed string.
"""

#Lesson 2 Lab 1
s = 'Python'
print(s[-2])
print(s[0:4])
print(s[1:4])
print(s[::-1])


#lesson 2 lab 2
l = [3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)


#lesson 2 lab 3
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
value_1 = d2['k1']
value_2 = value_1['k2']
print(value_2)

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
list_1 = d3['k1']
value_1 = list_1[0]
list_2 = value_1['nest_key']
list_3= list_2[1]
value_2 = list_3[0]
print(value_2)


#lesson 2 lab 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))


#lesson 2 lab 5
age = 4
name = 'Sammy'
print(f"Hello my dog's name is {name} and he is {age} years old")


#lesson 2 lab 6
base = int(input('please input base: '))
exponent= int(input('please input exponent: '))

power = 1
for _ in range(exponent):  #循环 exponent 次 = 3次
    power = power * base
print(power)

#base=2 exponent=3（loop 3 times)
#power = 1
#power = 1*2 = 2
#2*2=4
#4*2=8


#lesson 2 lab 7
tuple = (1, 4, 6)
print(sum(tuple))


#lesson 2 lab 8
given_tuple = (2, 5, 6, 8)
x, y, z, u = given_tuple
print(x)
print(z)
print(u)


#lesson 2 lab 9
dictionary_1 = {'name':'Bob', 'age':4}
dictionary_1 ['name'] = ['Alice']
print(dictionary_1)


#lesson 2 lab 10
list = [3, 6, 5, 8, 7]
even_numbers = [i for i in list if i % 2 == 0]
print(even_numbers)

#lesson 2 lab 11
string = input("input a string: ")
print(string[::-1])






#1210 class content
#find dictionary
my_dictionary = {
    1:'value one',
    2:'value two',
    3:'value three',
    4:['name_one','name_two'],
    4:['value?']
}

print(my_dictionary)
print(my_dictionary[4][0].upper())

#create new dictionary
new_dictionary = {}

new_dictionary['animal'] = 'cat'
new_dictionary['answer'] = 42
print(new_dictionary)

#nested dictionary 嵌套字典 dictionary within a dictionary
nested_dictionary = {
    'person1':{
        'age':30,
        'name':'bob',
    },
    'person2':{
        'age':20,
        'name':'alice'
    },
}

print(nested_dictionary)
#find alice

dictionary = {
    'key1' : 1,
    'key2' : 2,
    'key3' : 3
}

print(dictionary.keys()) #print all the keys
print(dictionary.values())
print(dictionary.items()) #print all the key value inside a tuple inside a list

#tuple can not change

my_tuple = (1,2,3,'four', 3)
#print(my_tuple)
#print(my_tuple[-1]) #using indexing to find
#print(my_tuple.index('four'))
#print(my_tuple.count(3)) #how many times elements in the tuple appears

#set & booleans unrepeat 不能重复的元素 unorganized无序的 mudable可变的

#x = set()
#x.add(1)
#print(x)

#可变的
#my_set = {1,2,3}
#my_set.add(4)
#print(my_set)

#不可重复
#my_set = {1,2,3}
#my_set.add(3)
#print(my_set)

my_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 6]
print(set(my_list)) #去重

#boolean
a = True
print(a) #output: True
print(1>2) #output: False

#control flow comparison operators
2>1
1<2
1<=1
1>=4
1==1
1!=2

print(1==1) #True
print(1 == '1') #False can't compare a int to a str
print('1' == '1') #True
print('hi' == 'bye') #False
print(1 != 2) #True

#logical operator and not or
(1 < 2) and (2 > 3) #True

(1 < 2) or (2 > 3) or (10 > 9)

#indentation 缩进 前面有空格
if 1 < 2:
    print('Yes!')

if 1 < 2:
    print('Yes!')
else:
    print('No!')

if 1 > 2:
    print('Yes!')
print('Hello') #no matter what i want to print out hello


if 1 == 2:
    print('first')
elif 3 ==3:         #else-if
    print('middle')
else:
    print('last')


#for Loops

sequence = [1,2,3,4,5]

for item in sequence:  #item can be x or i or num or any
    print(item)  #1 2 3 4 5 

for item in sequence:
    print('Yes') #Yes * 5 次 成一列

for apple in sequence:
    print(apple + apple) #2 4 6 8 10
    
for item in sequence:
    print('Yes', end= ' ') #output 成一行 不是一列,end是个function 后面是空格或者可以加其他- 
#for loop in dictionary 

ages = {
    'John': 4,
    'Doe': 8,
    'Moe': 5
}

for key in ages:
    print('This is the Key: ')
    print(key)
    print('This is the value: ')
    print(ages[key])
    print('\n')

#tuples in list For loop

#mypairs = [(1,10), (2,20), (3,30)] #tuple unpacking

#for tup in mypairs:
#    print(tup) #output (1,10) (2,20) (3,30)

#for item1, item2 in mypairs:
#    print(item1) # item1 is 1
#    print(item2) # item2 is 10 #output is 1 10 2 20 3 30

mypairs = [(1,10,11), (2,20,21), (3,30,31)] #tuple unpacking

for item1, item2, item3 in mypairs:
    print(item1) 
    print(item2)
    print(item3)
    
#while loops

i = 1
while i < 5: #while conditional
    print(f'i is: {i}')
    i = i + 1 #i += 1


