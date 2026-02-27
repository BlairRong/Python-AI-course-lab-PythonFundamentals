a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

a = int(input())
b = int(input())
print(a//b)
print(float(a/b))

n = int(input().strip())
for i in range(n):
    print(i * i)


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))

n = int(input())
for i in range(1, n+1):
    print(i, end="")



import numpy as np

def min_then_max(arr):
    # 第一步：沿着axis=1取最小值（每行的最小值）
    min_along_axis1 = np.min(arr, axis=1)
    print("每行的最小值:", min_along_axis1)
    
    # 第二步：对最小值结果取最大值
    result = np.max(min_along_axis1)
    return result

# 使用你提供的例子
my_array = np.array([[2, 5], 
                     [3, 7],
                     [1, 3],
                     [4, 0]])

print("原始数组:")
print(my_array)
print()

final_result = min_then_max(my_array)
print("最终结果:", final_result)


import numpy as np
def min_then_max(arr):
    return np.max(np.min(arr,axis=1))
    
my_array = np.array([[2, 5], 
                     [3, 7],
                     [1, 3],
                     [4, 0]])
print(min_then_max(my_array))

a=10
b=20
a=b
