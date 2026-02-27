"""
#square the list  平方列表
#loop 
numbers = [1, 2, 3, 4, 5]
squares = [ ]
for num in numbers:
    squares.append(num ** 2)
print(squares)
#[1, 4, 9, 16, 25]

#list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
#[1, 4, 9, 16, 25]


#find even number 找偶数 filtered过滤
#loop
numbers = [3, 6, 7, 9, 2, 6]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)
#[6, 2, 6]

#list comprehension
numbers = [3, 6, 7, 9, 2, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
#[6, 2, 6]


#upper str/words in list 转换字符串大写 
words = ['hello','world','python']
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(upper_words)
#['HELLO', 'WORLD', 'PYTHON']

#list comprehension
words = ['hello','world','python']
upper_words = [word.upper() for word in words]
print(upper_words)
#['HELLO', 'WORLD', 'PYTHON']


#结合条件转换 
#loop
numbers = [2, 4, 5, 7, 9]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num * 10)
    else:
        result.append(num)
print(result)
#[20, 40, 5, 7, 9]


#list comprehension
numbers = [2, 4, 5, 7, 9]
result = [num * 10 if num % 2 == 0 else num for num in numbers]
print (result)
#[20, 40, 5, 7, 9]


#嵌套循环 nested loop  把两个列表内容互相组合
#loop
pairs = []
for x in [1,2,3]:
    for y in ['a', 'b']:
        pairs.append((x,y))
print(pairs)
#[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]


#list comprehension
pairs = [(x,y) for x in [1,2,3] for y in ['a','b']]
print(pairs)
#[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]


#list comprehension 平方指定区间元素
squares = [num ** 2 for num in range(1,5)]
print(squares)
#[1, 4, 9, 16]



"""
