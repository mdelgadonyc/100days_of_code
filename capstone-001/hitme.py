# Day 11 Project: [Capstone] Blackjack: Hit me!


# Our Blackjack House Rules #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
cpu_hand = []


def final():
    print(f"Your final hand: {my_hand}")
    print(f"Computer's final hand: {cpu_hand}")

    my_total = sum(my_hand)
    cpu_total = sum(cpu_hand)

    if my_total > 21:
        print("You went over. You lose 😭")
    elif my_total == cpu_total:
        print("Draw 🙃")
    elif my_total == 21 and len(my_hand) == 2:
        print("Win with a Blackjack 😎")
    elif my_total == 21:
        print("You win")
    elif my_total > cpu_total:
        print("You win")
    else:
        print("You lose")


def draw():
    if not my_hand:
        # draw two cards for player
        my_hand.append(random.choice(cards))
        my_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
    else:
        my_hand.append(random.choice(cards))
        print(sum(my_hand))
        if sum(cpu_hand) < 17:
            cpu_hand.append(random.choice(cards))

    # print(f"Your cards: {my_hand}, current score: {sum(my_hand)}")
    if sum(cpu_hand) > 21:
        if 11 in cpu_hand:
            position = cpu_hand.index(11)
            my_hand[position] = 1

    if sum(my_hand) > 21:
        if 11 in my_hand:
            position = my_hand.index(11)
            my_hand[position] = 1
        else:
            final()
            return
    elif sum(my_hand) == 21:
        final()
        return

    print(f"Your cards: {my_hand}")
    print(f"Computer's first card: {cpu_hand[0]}")
    another = input("Type 'y' to get another card, type 'n' to pass: ")
    if another == 'y':
        draw()
    elif another == 'n':
        final()
        return


def begin():
    print(logo)

    my_hand.clear()
    cpu_hand.clear()

    draw()


# Loop as long as user wants to play a game
while 1:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_again == 'y':
        begin()
    elif play_again == 'n':
        exit()
