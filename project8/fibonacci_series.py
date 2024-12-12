# Fibonacci sequence
def fibonacci_sequence(n):
    # Fibonacci sequence start with first two digit 0, 1
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fb_sequence = [0, 1]

    for i in range(n - 2):
        next_num = fb_sequence[-1] + fb_sequence[-2]
        fb_sequence.append(next_num)
    
    return fb_sequence

print("🚀 Welcome to the Fibonacci Sequence Generator! 🚀")
while True:
    while True:
        n = input("Enter a number to generate fibonacci sequence (or 'q' to quit): ")
        if n == 'q':
            print("Goodbye!👋")
            exit()
        try:
            n = int(n)
            if n <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except:
            print("Not a valid number!")

    fb_sequence = fibonacci_sequence(n)
    print(f"📈Fibonacci sequence({n} numbers): {', '.join(str(x) for x in fb_sequence)}")
