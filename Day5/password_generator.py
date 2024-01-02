#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
password_list = []
for letter in range(0, nr_letters):
    #tmp = letters[random.randint(0, len(letters)-1)]
    tmp = random.choice(letters)
    password += tmp
    password_list.append(tmp)
for letter in range(0, nr_symbols):
    #tmp = symbols[random.randint(0, len(symbols)-1)]
    tmp = random.choice(symbols)
    password += tmp
    password_list.append(tmp)
for letter in range(0, nr_numbers):
    #tmp = numbers[random.randint(0, len(numbers)-1)]
    tmp = random.choice(numbers)
    password += tmp
    password_list.append(tmp)

print(password)
print(password_list)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
randomised_password = ""
random.shuffle(password_list)
for val in password_list:
    randomised_password += val
print(randomised_password)