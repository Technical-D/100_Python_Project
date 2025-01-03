# Variable 
name = "Dheeraj"
number = 10
decimal = 1.1
boolean = True 

# print(f"Name: {name}, number: {number}, decimal: {decimal}, boolean: {boolean}")

# name = str(input("Your Name: "))
# age = int(input("Your age: "))

# print(f"Name: {name}, Age:{age}")
# print(type(name), type(age))

# for i in range(-10,11,1): # -10 is start number , 11 is edning, 1 is the increased from
#     print(i)

# Sorting the list based on len of string inside the list
# name = ["dheeraj", "jay", "shubham", "anjali"]
# def get_len(l):
#     return len(l)

# name.sort(reverse=True,key=get_len)
# print(name)

# Try and except
# n = [1,3,4,5,6]
# try:
#     x = n.index(7)
# except ValueError:
#     print("Value not found!")

# ZIP
# a = [1,2,3]
# b = ['a', 'b', 'c']
# c = ['!', '@', '#']

# for i,j,k in zip(a,b,c):
#     print(i,j,k)

# for i in range(3, 10, 2):
#     print(i)

# items = {"dhh": 12, "dhdh":13, "etey": 17}

# for key in items.keys():
#     print(key)

# for value in items.values():
#     print(value)

# for key, value in items.items():
#     print(key, value)

# Conditional Statement
# if True:
#     print("Hello")

# return false
# if 1 == '1':
    # print(1)

# val = [1,1,4,5,7]
# return the max sum of 3 number in list
# val = sorted(val, reverse=True)
# max_sum = sum(val[:3])
# print(max_sum)

# Finding smallest num in list
# list_1 = [1,4,5,6,71,3]
# smallest_num = None
# for num in list_1:
#     if smallest_num is None or num < smallest_num:
#         smallest_num = num
# print(smallest_num)

# Finding largest num in list
# largest_num = None
# for num in list_1:
#     if largest_num is None or num > largest_num:
#         largest_num = num
# print(largest_num)

from time import sleep
for i in range(10, -1,-1):
    print(i)
    sleep(1)