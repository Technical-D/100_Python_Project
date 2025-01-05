# Tree pattern
#         *        
#        ***       
#       *****      
#      *******     
#     *********    
#    ***********
#   *************
#  ***************
# *****************
#         *
def tree(height):
    height = height - 1
    length = height * 2 - 1
    star = 1
    for i in range(1, height + 1):
        print(("*" * star).center(length))
        star += 2
    print("*".center(length), end="")

while True:
    # n = input("Enter a height of tree: ")
    try:
        # n = int(n)
        break
    except:
        print("Please enter a valid number!")

# Drawing tree
# print("Here is your tree:\n ")
# tree(n)


# Left-aligned Triangle 
n = 10
# for i in range(1,n+1):
    # print("*" * i)

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

# Right Triangle
# for i in range(1, n+1):
    # print(" " * (n-i) + "*" * i)

#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********

# Left-aligned Reverse Triagnle
# for i in range(n, 0, -1):
#     print("*" * i)

# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

# Right-aligned Reverse triangle
# for i in range(n, 0, -1):
#     print(" " * (n-i) + "*" * i)

# Symmetric Triangle
# l = n * 2 -1
# stars = 1
# for i in range(1, n+1):
#     print(("*" * stars).center(l))
#     stars += 2

# Without center method
height = 10
length = height * 2 - 1
s = 1
for i in range(1, height+1):
    space = (length - s) // 2
    print(" " * space + "*" * s)
    s += 2