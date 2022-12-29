from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    new_text = ''
    for letter in text:
        if not letter.isalpha():
            new_text += letter
        else:
            index = alphabet.index(letter)
            if direction == 'encode':
                new_index = index + shift
            elif direction == 'decode':
                new_index = index - shift
            new_text += alphabet[new_index]
    print(f"the {direction}d text is '{new_text}'")

print(logo)

cont = True

while cont:
    bad_input = True
    while bad_input:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            bad_input = False
        else:
            print('Not a valid response. Please type that again.')
    no_text = True
    while no_text:
        text = input("Type your message:\n").lower()
        if len(text)  > 0:
            no_text = False
        else:
            print("No text to encode/decode. Please type the text you wish to encode/decode.")
    shift = int(input("Type the shift number:\n"))
        
    if shift > 26:
        shift = shift % 26

    caesar(direction, text, shift)

    try_again = True
    while try_again:
        more = input('Would you like quit? yes or no:\n').lower()
        if more == 'yes':
            cont = False
            try_again = False
            print('Goodbye.')
        elif more == 'no':
            try_again = False
        else:
            print('Not a valid response. Please type that again.')