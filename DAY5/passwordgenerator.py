import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '~', '`']


print("Welcome to the PyPasswrod Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

set_of_random_numbers = ''
for number in range(0, nr_numbers):
    randNumber = random.choice(numbers)
    set_of_random_numbers += randNumber

set_of_random_letters = ''
for letter in range(0, nr_letters):
    randLetter = random.choice(letters)
    set_of_random_letters += randLetter

set_of_random_symbols = ''
for symbol in range(0, nr_symbols):
    randSymbol = random.choice(symbols)
    set_of_random_symbols += randSymbol

password_code = set_of_random_symbols + set_of_random_letters + set_of_random_numbers
password_characters = list(password_code)
random.shuffle(password_characters)
password = ''.join(password_characters)
print(f'Here is your password: {password}')