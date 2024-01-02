# Data types

# String
# Subscript []
print("Hello"[4])

#Integers
print(123 + 345)

# large numbers can be rep as below for more readability
large_int = 12_34_56_789
print(large_int)

# Float 57.25

#Boolean  True or False

# TypeError
# TypeChecking
# TypeConversion

two_digit_number = input()
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Mathematical operators
# + , - , *, / , ** (exponents)
# PE MD AS and left to right calculation
# () ** * / + -

print(3 * 3 + 3 / 3 - 3)


# 1st input: enter height in meters e.g: 1.6534
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

print(int(int(weight)/ (float(height)**2)))


# round function

print(round(8/3, 2))

#f-string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height} and you are winning is {isWinning}")


age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")