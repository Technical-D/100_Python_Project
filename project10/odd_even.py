# Odd Even Checker
def is_odd_or_even(n):
    if n % 2 == 0:
        return True
    return False

print("Welcom to Odd Even Checker!")
print("This program will tell you if a number is Odd or Even.")
while True:
    num = input("Enter a number or type 'q' to quit: ")
    try:
        num  = int(num)
        if num == 0:
            print("0 is an Even number!")
            continue

        if is_odd_or_even(num):
            print(f"{num} is an Even number!")
        else:
            print(f"{num} is an odd number!")
    except:
        if num.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number or command!")

        