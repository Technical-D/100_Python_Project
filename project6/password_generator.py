# Password Generator
import random

def generate_password(n,include_number,include_special_char, include_uppercase_char):
    number = "0123456789"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_char = "!@#$%&*"

    mash_up = alphabet
    if include_number:
        mash_up += number
    if include_special_char:
        mash_up += special_char
    if include_uppercase_char:
        mash_up += uppercase_alphabet

    password = ''.join(random.choice(mash_up) for _ in range(n))
    
    return password

print("Welcome to Password Generator!")
while True:
    length = input("Enter the length of the password: ")
    try:
        length = int(length)
        if length < 4:
            print("Password length should be at least 4 characters.")
            continue
        break
    except:
        print("Inavlid number! Please enter a valid number.")

while True:
    include_number = input("Include the numbers (y/n): ").lower()
    if include_number in ['y', 'n']:
        include_number = (include_number == 'y')
        break
    else:
        print("Invalid Input! Please enter 'y' for yes and 'n' for no.")

while True:
    include_special_char = input("Include special charachter (y/n): ").lower()
    if include_special_char in ['y', 'n']:
        include_special_char = (include_special_char == 'y')
        break
    else:
        print("Invalid Input! Please enter 'y' for yes and 'n' for no.")

while True:
    include_uppercase_char = input("Include Uppercase alphabet (y/n): ").lower()
    if include_uppercase_char in ['y', 'n']:
        include_uppercase_char = (include_uppercase_char == 'y')
        break
    else:
        print("Invalid Input! Please enter 'y' for yes and 'n' for no.")

password = generate_password(length, include_number, include_special_char, include_uppercase_char)
print(f"🎉 Your generated password is: {password}")


