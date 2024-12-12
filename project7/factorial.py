# Factorial
print("🚀 Welcome to the Factorial Calculator! 🚀")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


while True:
    while True:
        n = input("Enter a non-negative number to calculate the factorial (or 'q' to quit): ")
        if n.lower() == 'q':
            print("Goodbye! 👋")
            exit()
        try:
            n = int(n)
            if n < 0:
                print("Enter a Positive number.")
                continue
            break
        except:
            print("Enter a valid number!")

    output = factorial(n)
    print(f"🎉 Factorial of {n} is {output} 🎉")
    print()
