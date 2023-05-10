# Day 9 Project: Silent Bid Auction

# 
from replit import clear
#HINT: You can call clear() to clear the output in the console.

# Display ASCII logo
from art import logo

print(logo)

print("Welcome to the secret auction program.")
names = []
bids = []
max_bid = ["", 0]

while (1):
    names.append(input("What is your name?: "))
    bids.append(input("What's your bid?: $"))
    
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if more == 'no':
        break
    clear()

# Locate the highest bid
for count, bid in enumerate(bids):
    bid = int(bid)
    
    if bid > max_bid[1]:
        max_bid[1] = bid
        max_bid[0] = names[count]

print(f"The winner is {max_bid[0]} with a bid of ${max_bid[1]}.")
        



