# Number Guessing
import random
import math

def random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

print("Welcome to Number Guessing Game!")
print("Please select range for number.")
while True:
    l = input("Enter lower bound: ")
    u = input("Enter upper bound: ")
    try:
        l, u = int(l),  int(u)
        if l < 0 or u < 0:
            print("Please enter a valid bounds!")
            continue

        if l > u:
            print("Lower bound must be less than or equal to upper bound!")
            continue
        break
    except:
        print("Please enter a valid number!")

total_chances = int(math.log2(u - l + 1))
n = random_number(l,u)
print(f"You've only {total_chances} chances to guess the number!")
print("Start....")
while total_chances > 0:
    while True:
        guess = input("Guess a number: ")
        try:
            guess = int(guess)
            break
        except:
            print("Please enter a valid number!")

    total_chances -= 1
    if guess == n:
        print("You've guessed it right. Congratulations!")
        break
    else:
        range_size = u - l
        diff = abs(guess - n)
        if diff <= range_size * 0.1:
            print("Very close! Try again.")
        elif diff <= range_size * 0.25:
            print("Close! Try again.")
        else:
            print("Way off! Try again.")

        if total_chances != 0:
            print(f"You've only {total_chances} chances remaining!")

    if total_chances == 0:
        print("Oops! You've used all your chances")
        print(f"The number is {n}.")
        print("Better luck next time!")