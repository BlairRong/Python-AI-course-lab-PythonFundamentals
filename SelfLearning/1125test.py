a=10
b=20
a=b
print(a)


s = "Hello" 
print(s[:-1])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_values = set(mylist)
print(unique_values)



def arrayCheck(numbers):
    for i in range ( len ( numbers ) -2) :
          if numbers [i] == 1 and
numbers [i+1] ==2 and numbers [i+2] ==3:
        return True
    return False



print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]) )

def count_evens(numbers):
    count = 0
    for number in numbers:
         if number % 2 == 0:
                count +=1
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))