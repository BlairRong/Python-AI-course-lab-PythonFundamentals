s="HelloWorld"
print(s[::2])

def stringBits(s):
    return(s[::2])
print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


def arrayCheck(numbers):
    for i in range(len(numbers) - 2):
        if numbers[i] == 1 and numbers[i+1] == 2 and numbers[i+2] == 3:
            return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3])) 



def factorial(n):
    if n == 1:       # base case
        return 1
    return n * factorial(n - 1)