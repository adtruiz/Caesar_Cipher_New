from art import logo
from alphabet import alphabet

should_end = False

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:  # if the character is in the alphabet list.....
            end_text += alphabet[alphabet.index(char) + shift_amount]
        else:  # if the character is not in the alphabet list.....
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 #  if the shift amount is greater than the letters in the alphabet, it will minimize it.

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
