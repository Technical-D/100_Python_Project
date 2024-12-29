# Ceaser Cipher 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    encrypted_text = ""

    for letter in plain_text:
        if letter in alphabet:
            postion = alphabet.index(letter)
            new_postion = postion + shift_amount

            if new_postion > len(alphabet) - 1:
                new_postion -= len(alphabet)

            encrypted_text += alphabet[new_postion]
        else:
            encrypted_text += letter

    return encrypted_text

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for letter in encrypted_text:
        if letter in alphabet:
            postion = alphabet.index(letter)
            new_postion = postion - shift_amount

            if new_postion < 0:
                new_postion += len(alphabet)
            
            decrypted_text += alphabet[new_postion]
        else:
            decrypted_text += letter
    
    return decrypted_text

print("Welcome to Ceaser Cipher Encryption Center!")

while True:
    plain_text = input("Enter a text to encrypt or type 'q' to quit: ").lower()
    if plain_text == 'q':
        print("Goodbye!")
        break

    while True:
        shift_amount = input("Enter a shift amount for the encrypton between 1 to 10: ")
        try:
            shift_amount = int(shift_amount)
            if not 1 <= shift_amount <= 10:
                print("Please enter a shift amount in given range.")
                continue
            break
        except:
            print("Please enter a valid number!")

    encrypted_text = encrypt(plain_text, shift_amount)
    decrypted_text = decrypt(encrypted_text, shift_amount) 
    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")
    print()

