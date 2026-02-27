def arrayCheck(numbers):
    for i in range ( len ( numbers ) -2) :
          if numbers [i] == 1 and numbers [i+1] ==2 and numbers [i+2] ==3:
               return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


def stringBits(s):
    return s[::2]

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


def count_evens(numbers):
    count = 0
    for number in numbers:
         if number % 2 == 0:
                count +=1
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))

