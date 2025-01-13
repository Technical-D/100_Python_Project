# Bagels, a deductive logic game
import random

num_digit = 3
max_guess = 10

def main():
    print(f"""
Bagels, a deductive logic game.
I am thinking of a {num_digit}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
""")
    while True:
        secret_num = get_secret_num(num_digit)
        print("I have thought up a number.")
        print(f"You have {max_guess} guesses to get it.")

        guess_num = 1
        while guess_num <= max_guess:
            guess = ''
            while len(guess) != num_digit or not guess.isdecimal():
                print(f"Guess #{guess_num}")
                guess = input(">")
            
            guess_num += 1
            if guess == secret_num:
                print("You got it!")
                break
            else:
                clues = get_clues(secret_num, guess)
                print(clues)

            if guess_num > max_guess:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")
        
        choice = input("Do you want to play again? y/n").lower()
        if choice == 'y':
            continue
        elif choice == 'n':
            break
    print("Thanks for playing!")

def get_secret_num(num_digit):
    numbers = list("0123456789")
    random.shuffle(numbers)
    secret_num = ''
    for i in range(num_digit):
        secret_num += str(numbers[i])

    return secret_num

def get_clues(secret_num, guess):
    clues = []

    for i in range(len(secret_num) - 1):
        if secret_num[i] == guess[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ''.join(clues)
        
if __name__ == '__main__':
    main()