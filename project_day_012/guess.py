# Day 12 Project: You Guessed It!

import random
from art import logo

guesses = 0

print(logo)

print("Welcome to the Number Guessing Game!")

# generate random number between 1 and 100
secret_num = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    guesses = 10
elif difficulty == 'hard':
    guesses = 5

while (guesses > 0):
    print(f"You have {guesses} attempts remaining to guess the number.")
    my_guess = int(input("Make a guess: "))
    if my_guess == secret_num:
        # hit!
        print(f"You got it! The answer was {secret_num}.")
        break
    elif my_guess > secret_num:
        print("Too high.")
    else:
        print("Too low.")
    guesses -= 1
