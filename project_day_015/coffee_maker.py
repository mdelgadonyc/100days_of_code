# Day 15 Project: Coffee Machine

BEVERAGE_MENU = ["espresso", "latte", "cappuccino"]
ESPRESSO = {
    "water": 1,
    "milk": 1,
    "coffee": 1,
    "price": 0
}

LATTE = {
    "water": 1,
    "milk": 1,
    "coffee": 1,
    "price": 0
}

CAPPUCCINO = {
    "water": 1,
    "milk": 1,
    "coffee": 1,
    "price": 0
}

resources_level = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "money": 0
}

machine_on = True


def turn_machine_off():
    global machine_on
    machine_on = False


# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def generate_report():
    print(f"water level: {resources_level['water']}ml")
    print(f"milk level: {resources_level['milk']}ml")
    print(f"coffee level: {resources_level['coffee']}g")
    print(f"money available: ${resources_level['money']}")


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(beverage):
    if beverage == "espresso":
        if ESPRESSO["water"] > resources_level["water"]:
            print("Sorry there is not enough water.")
            return False
        elif ESPRESSO["milk"] > resources_level["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif ESPRESSO["coffee"] > resources_level["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif beverage == "latte":
        if LATTE["water"] > resources_level["water"]:
            print("Sorry there is not enough water.")
            return False
        elif LATTE["milk"] > resources_level["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif LATTE["coffee"] > resources_level["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif beverage == "cappuccino":
        if CAPPUCCINO["water"] > resources_level["water"]:
            print("Sorry there is not enough water.")
            return False
        elif CAPPUCCINO["milk"] > resources_level["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif CAPPUCCINO["coffee"] > resources_level["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True


def request_payment():
    pass


def start_machine():

    while machine_on:

        # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice in BEVERAGE_MENU:
            if check_resources(coffee_choice):
                request_payment()
        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        elif coffee_choice == "off":
            turn_machine_off()
        elif coffee_choice == "report":
            generate_report()

# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.


start_machine()


"""
Coffee Machine Program Requirements

4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""