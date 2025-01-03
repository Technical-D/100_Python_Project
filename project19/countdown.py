# Countdown
from time import sleep
import winsound

print("Welcome to Countdown App!")

while True:
    n = input("Enter a number to start countdown: ")
    try:
        n = int(n)
        break
    except ValueError as e:
        print("Please enter a valid number!")

print("Countdown start: ")
for i in range(n, -1, -1):
    print(f"Time remaining: {i} seconds")
    winsound.Beep(1000, 500)
    sleep(1)
    

print("Time's up!")
winsound.Beep(3000, 1000)