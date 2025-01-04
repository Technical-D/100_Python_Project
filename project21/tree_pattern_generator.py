# Tree pattern
def tree(height):
    height = height - 1
    length = height * 2 - 1
    star = 1
    for i in range(1, height + 1):
        print(("*" * star).center(length))
        star += 2
    print("*".center(length), end="")

print("Welcom to Tree Pattern Generator!")

while True:
    n = input("Enter a height of tree: ")
    try:
        n = int(n)
        break
    except:
        print("Please enter a valid number!")

# Drawing tree
print("Here is your tree:\n ")
tree(n)