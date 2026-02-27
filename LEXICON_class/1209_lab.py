
#1209 Lab

"""
Lab 1 --Python Calculator(Numbers & Arithmetic 算术)
Create a program that:
1. Takes two numbers from the user
2. Calculates and prints:
o Sum
o Difference
o Product
o Division
o Power
3. Print the results in a nicely formatted way.
Goal: Practice numeric operations & print formatting.

LAB 2 — Variables 变量 & Reassignment 重新赋值
Students must:
1. Create variables for salary, bonus, and tax_rate.
2. Calculate:
o total income
o taxes
o net income
3. Reassign variables to simulate a raise and recalc everything.
Goal: Understand variable assignment and updating values.

LAB 3 — String Indexing & Slicing Explorer
Given the string:
s = "ProgrammingIsFun"
Students must extract:
1. The first letter
2. The last 3 letters
3. Every second letter
4. The word "Programming"
5. The word "Fun" without using indices directly (must use slicing)
6. The string reversed
Goal: Practice indexing, slicing, stepping.

LAB 4 — String Methods Investigation
Using a string from user input, students must show:
1. Uppercase version
2. Lowercase version
3. How many characters the string has
4. Split the string into words
5. Replace one letter with another
Goal: Practice built-in string methods & transformations.

LAB 5 — Username Generator
Ask the user for:
• First name
• Last name
• Birth year
Then generate a username using slicing, for example:
first 2 letters of first name + last 3 letters of last name + last 2 digits of birth year
Goal: Combine indexing, slicing, formatting, variables.

LAB 6 — List Builder
Students must:
1. Create a list with 5 mixed-type elements
2. Use append() to add two new items
3. Use pop() to remove an element
4. Reverse the list
5. Sort the list (if possible)
6. Print the final result
Goal: Practice list manipulation.

LAB 7 — Shopping Cart Program
Simulate a shopping cart using lists.
Steps:
1. 2. 3. Start with an empty list cart = []
Ask user 5 times to input an item and append it
After all items are added:
o Print the full cart
o Remove the last item
o Show how many items remain
o Print only the first and last items
Goal: Combine lists, len(), append(), pop(), indexing.

LAB 8 — Matrix Navigation
Create three lists and nest them to form a matrix. Example:
[ [1,2,3],
[4,5,6],
[7,8,9] ]
Students must:
1. Print the number in row 1, column 2
2. Print the entire second row
3. Print the diagonal (1,5,9)
4. Create a new list of all first-column elements using indexing
5. Then repeat using a list comprehension 列表推导式
Goal: Practice nesting + comprehensions.

LAB 9 — List Comprehension Transformations
Given:
numbers = [1,2,3,4,5,6,7,8,9]
Students must create using list comprehensions:
1. A list of squares
2. 3. 4. 5. A list of only even numbers
A list of numbers doubled
A list of only numbers greater than 5
A list of strings: "Number: X" for each element
Goal: Become comfortable with comprehensions.

LAB 10 — Mini Project: Student Information Formatter
Ask user for:
• Name
• Age
• Favorite subject
• Favorite quote
Then:
1. Use formatting (.format() or f-strings) to print a nicely formatted paragraph.
2. Capitalize the name.
3. Remove whitespace around inputs.
4. Create a list of the letters from the name.
5. Print the first and last letter from that list.
Goal: Combine strings, formatting, indexing, list creation.

"""

#answer
#Lab 1
number_a = int(input("> "))
number_b = int(input("> "))

print(f'Sum is {number_a + number_b}')
print(f'Difference is {number_a - number_b}')
print(f'Product is {number_a * number_b}')
print(f'Division is {number_a / number_b}')
print(f'Power is {number_a ** number_b}')


#Lab 2
salary = 10000
bonus = 2000
tax_rate = 0.2

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print(f'total income: {total_income}')
print(f'taxes: {taxes}')
print(f'net income: {net_income}')

salary = 20000
bonus = 2000
tax_rate = 0.2

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print(f'total income: {total_income}')
print(f'taxes: {taxes}')
print(f'net income: {net_income}')


#Lab 3
s = "ProgrammingIsFun"
print(s[0:1])
print(s[13:])
print(s[::2])
print(s[0:11])
start_index = s.find("Fun")
result = s[start_index : start_index + 3] #don't understand
print(result)
print(s[::-1])


#Lab 4
user_string = input('')
uppercase_version = user_string.upper()
lowercase_version = user_string.lower()
characters_count = len(user_string)
split_version = user_string.split()
replace = user_string.replace('o', '@')

print(f'Uppercase version is {uppercase_version}')
print(f'Lowercase version is {lowercase_version}')
print(f'Characters count is {characters_count}')
print(f'Slit the string into {split_version}')
print(f'Replaced version {replace}')

#Lab 5
first_name = input("First name: ")
last_name = input("Last name: ")
birth_year = input("Birth year: ")

first_2_letters_of_first_name = first_name[0:2]
last_3_letters_of_last_name = last_name[-3:]
last_2_digits_of_birth_year = birth_year[-2:]

print(first_2_letters_of_first_name+last_3_letters_of_last_name+last_2_digits_of_birth_year)

#Lab 6
mixed_list = [2, 'Hello', 3.4, True, "World"]

mixed_list.append(5)
mixed_list.append(False)
removed_element = mixed_list.pop(2)
mixed_list.reverse()

print(mixed_list)


#Lab 7
cart = []

input_times = 0
input_limit = 5
while input_times < input_limit:
    item_name = input("Input an item name: ")
    cart.append(item_name)
    input_times += 1
print(cart)

remover_last_item = cart.pop()
print(cart)

print(len(cart))

first_item = cart[0]
last_item = cart[-1]

print(f'{first_item} {last_item}')

#Lab 8
lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("original lists: ")
for row in lists:
    print(row)
print()

print(lists[0][1])

print(lists[1])
#3
diagonal_1 = lists[0][0]
diagonal_2 = lists[1][1]
diagonal_3 = lists[2][2]
print(f'({diagonal_1}, {diagonal_2}, {diagonal_3})')
#or
diagonal = []
for i in range(3):
    diagonal.append(lists[i][i])
print(f'{diagonal}')
#4
new_list_1 = lists[0][0]
new_list_2 = lists[1][0]
new_list_3 = lists[2][0]
print(f'[{new_list_1}, {new_list_2}, {new_list_3}]')
#or
first_column = []
for i in range(3):
    first_column.append(lists[i][0])
print(first_column)
#5 格式[lists[i][列] for i in range(n)]
first_column_comprehension = [lists[i][0] for i in range(3)]
print(first_column_comprehension)

#Lab 9
numbers = [1,2,3,4,5,6,7,8,9]
#squares=平方数 even=双数/偶数
#1
squares = [i ** 2 for i in range (1,10)]
print(squares)
#2
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)
#3
doubled_numbers = [i * 2 for i in numbers]
print(doubled_numbers)
#4
greate_than_5 = [i for i in numbers if i > 5]
print(greate_than_5)
#5
string = [f'Number: {i}' for i in numbers]
print(string)

#Lab 10
name = input("Name: ")
age = input("Age: ")
subject = input("Favorite subject: ")
quote = input("Favourite quote: ")

#1
print(f"My name is {name}, my age is {age}, my favorite subject is {subject}, my favorite quote is {quote}.")
#2
print(name.capitalize())
#3
print(name.strip())
#4
name_without_space = name.replace(" ","")
letters_list =list(name_without_space)
print(letters_list)
#5
first_letter = letters_list[0]
last_letter = letters_list[-1]
print(f'{first_letter}, {last_letter}')





#1209 class content
#list

my_list = ['one','two','three',4, 5]

my_list = my_list + ['new_item']

print(my_list)

my_list = ['one','two','three',4, 5]

print(my_list * 2) #not permenet

print(my_list)


l = [1,2,3]

l.append("append me!")
print(l)

l = [1,2,3]

l.append("append me!")
poppoed_item = l.pop(0)
print(poppoed_item)


new_list = ['a','e','x','b','c']
new_list.reverse()
print(new_list)

new_list = ['a','e','x','b','c']
new_list.sort()
print(new_list)

new_list = ['a','e','x',1, 2]
new_list.sort()
print(new_list)
#not working  need to have same int or same str

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

matrix = [lst_1, lst_2, lst_3]

print(matrix[0][0])

#matrix

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

matrix = [lst_1, lst_2, lst_3]

first_col = [row[0] for row in matrix]
print(first_col)