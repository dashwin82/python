import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.

rand_int = random.randint(0, (names.__len__() - 1))

print(f"{names[rand_int]} is going to buy the meal today!")