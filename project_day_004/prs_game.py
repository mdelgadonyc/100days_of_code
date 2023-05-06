# Day 4 Project: Rock, Paper, Scissors - Game On!

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
import random

def draw():
  print("It's a draw!")

def win():
  print("You win!")

def lose():
  print("You lose!")
  
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice = int(user_choice)
if user_choice > 2 or user_choice < 0:
  print("You chose an invalid number, you lose!")
  exit()
  
game_choices = [rock, paper, scissors]
print(game_choices[user_choice])

cpu_choice = random.randint(0,2)
print("\n\nComputer chose:")
print(game_choices[cpu_choice])

# implement game rules
if user_choice == cpu_choice:
  draw()
elif user_choice == 0 and cpu_choice == 1:
  lose()
elif user_choice == 0 and cpu_choice == 2:
  win()
elif user_choice == 1 and cpu_choice == 0:
  win()
elif user_choice == 1 and cpu_choice == 2:
  lose()
elif user_choice == 2 and cpu_choice == 0:
  lose()
elif user_choice == 2 and cpu_choice == 1:
  win()
