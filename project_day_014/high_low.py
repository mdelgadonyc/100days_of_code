
# Day 14 Project: Higher/Lower Game

from game_data import data
import random
from art import logo, vs

score = 0

def get_game_item():
    item = random.choice(data)
    return f'{item["name"]}, a {item["description"]}, from {item["country"]}', item["follower_count"]


def who_has_more(a_followers, b_followers):
    if a_followers > b_followers:
        return 'A'
    else:
        return 'B'


def win_round():
    global score
    score += 1
    # clear the screen
    # clear()
    print(logo)
    print(f"You're right! Current score: {score}.")


def game_over():
    print(f"Sorry, that's wrong. Final score: {score}")
    exit()


def start_game():
    print(logo)

    options = {}

    while (1):
        
        if not options:
            options['A'] = get_game_item()
        
        print(f"Compare A: {options['A'][0]}.")

        print(vs)
        options['B'] = get_game_item()
        while options['B'] == options['A']:
            options['B'] = get_game_item()

        print(f"Against B: {options['B'][0]}.")
        
        response = input("Who has more followers? Type 'A' or 'B': ").upper()
        if response == who_has_more(options['A'][1], options['B'][1]):
            win_round()
            options['A'] = options['B']
        else:
            game_over()


start_game()