# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_value = (weight / (height ** 2))

if bmi_value < 18.5:
    print(f"Your BMI is {bmi_value}, you are underweight.")
elif bmi_value > 18.5 and bmi_value < 25:
    print(f"Your BMI is {bmi_value}, you have a normal weight.")
elif bmi_value >= 25 and bmi_value < 30:
    print(f"Your BMI is {bmi_value}, you are slightly overweight.")
elif bmi_value >=30 and bmi_value < 35:
    print(f"Your BMI is {bmi_value}, you are obese.")
else:
    print(f"Your BMI is {bmi_value}, you are clinically obese.")