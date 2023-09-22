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
---'
'''
choices2 = input("Type 0 for rock, 1 for paper and 2 for scissors! ")
choices1 = [rock, paper, scissors]
computer_choice = random.choice(choices1)
#matching input to the variables
if choices2 == "0":
    choices2 = rock
    print(choices2)
elif choices2 == "1":
    choices2 = paper
    print(choices2)
elif choices2 == "2":
    choices2 = scissors
    print(choices2)
print("Computer's choice: ")
print(computer_choice)
if choices2 == rock and computer_choice == scissors:
    print("You Win!")
elif choices2 == scissors and computer_choice == paper:
    print("You Win!")
elif choices2 == paper and computer_choice == rock:
    print("You Win!")
elif choices2 == computer_choice:
    print("You have a tie!")
else:
    print("You Lose!")