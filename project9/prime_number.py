# Prime Number Factory
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):  
        if num % i == 0:
            return False
    return True

def prime_number_checker():
    print()
    print("--Prime Number Checker--")
    while True:
        n = input("Enter a number greater than 0 to check if it's prime: ")
        try:
            n = int(n)
            if is_prime(n):
                print(f"{n} is a prime number!")
            else:
                print(f"{n} is not a prime number!")
            break
        except:
            print("Please enter a Valid number!")

def prime_number_generator():
    print()
    print("--Prime Number Generator--")
    while True:
        r = input("Enter two numbers (start and end) separated by a space: ").split()
        try:
            start, end = int(r[0]), int(r[1])
            if start < 0 or end < 0:
                print("Please enter numbers greater than or equal to zero!")
                continue

            if start > end or start == end:
                print("Please enter a valid range!")
                continue

            prime_number = [i for i in range(start, end+1) if is_prime(i)]
            print("Prime numbers:")
            print(", ".join(map(str, prime_number)))
            break
        except:
            print("Please enter a valid range!")    

print("Welocme to Prime Number Factory!") 
print("Prime Number Checker(c) --or-- Prime Number Generator(g)")
while True:
    choice = input("Enter corresponding alphabet to enter that field or (q) to quit: ").lower()
    if choice == 'c':
        prime_number_checker()
    elif choice == 'g':
        prime_number_generator()
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice!(c/g/q)")




