import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_let = random.choices(letters, weights=None, cum_weights=None, k = nr_letters)
rand_num = random.choices(numbers, weights=None, cum_weights=None, k = nr_numbers)
rand_char = random.choices(symbols, weights=None, cum_weights=None, k = nr_symbols)

pwd = list()
for x in rand_let:
    pwd.append(x)
for x in rand_char:
    pwd.append(x)
for x in rand_num:
    pwd.append(x)

random.shuffle(pwd)

new_pwd = ''
for char in pwd:
    new_pwd += char

print(f"Your new passord is: {new_pwd}")
