import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice_list = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors")
user_choice = int (input())
print(choice_list[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{choice_list[computer_choice]}")

if user_choice == computer_choice:
    print ("Draw")
elif user_choice == 0:
    if computer_choice == 1:
        print ("You Lose")
    else:
        print ("You Won")
elif user_choice == 1:
    if computer_choice == 0:
        print ("You Won")
    else:
        print ("You Lose")
elif user_choice == 2:
    if computer_choice == 1:
        print ("You Won")
    else:
        print ("You Lose")
