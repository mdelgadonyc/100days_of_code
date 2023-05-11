# Day 11 Project: [Capstone] Blackjack: Hit me!

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
cpu_hand = []

def final():
    print(f"Your final hand: {my_hand}")
    print(f"Computer's final hand: {cpu_hand}")

    my_total = sum(my_hand)
    print(my_total)
    cpu_total = sum(cpu_hand)

    if my_total > 21:
        print("You went over. You lose")
    elif my_total == cpu_total:
        print("Draw")
    elif my_total > cpu_total:
        print("You win")

    #determine winner and print
    #print("You Win")
    #print("You Lose")

def draw():
    if not my_hand:            
        # draw two cards for player
        my_hand.append(random.choice(cards))
        my_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
    else:
        my_hand.append(random.choice(cards))
        if sum(cpu_hand) < 17:
            cpu_hand.append(random.choice(cards))

    #print(f"Your cards: {my_hand}, current score: {sum(my_hand)}")
    if sum(my_hand) > 21:
        final()

    print(f"Your cards: {my_hand}")
    print(f"Computer's first card: {cpu_hand[0]}")

def begin():
    print(logo)
    
    draw()
    
    response = input("Type 'y' to get another card, type 'n' to pass: ")
    if response == 'y':
        draw()
    elif response == 'n':
        final()


# Loop as long as user wants to play a game
while(1):
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if response == 'y':
        begin()

