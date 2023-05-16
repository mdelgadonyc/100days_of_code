# Day 15 Project: Coffee Machine

BEVERAGE_MENU = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "price": 1.50
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "price": 2.50
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "price": 3.00
    }}

resources_level = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_on = True


def turn_machine_off():
    global machine_on
    machine_on = False


def generate_report():
    print(f"water level: {resources_level['water']}ml")
    print(f"milk level: {resources_level['milk']}ml")
    print(f"coffee level: {resources_level['coffee']}g")
    print(f"money available: ${resources_level['money']:.2f}")


def check_resources(beverage):
    if BEVERAGE_MENU[beverage]["water"] > resources_level["water"]:
        print("Sorry there is not enough water.")
        return False
    elif BEVERAGE_MENU[beverage]["milk"] > resources_level["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif BEVERAGE_MENU[beverage]["coffee"] > resources_level["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def request_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies: "))
    total = round(0.25 * quarters + 0.10 * dimes + .05 * nickles + .01 * pennies, 2)
    return total


def serve_beverage(coffee_choice):
    resources_level['money'] += BEVERAGE_MENU[coffee_choice]["price"]

    resources_level["water"] -= BEVERAGE_MENU[coffee_choice]["water"]
    resources_level["milk"] -= BEVERAGE_MENU[coffee_choice]["milk"]
    resources_level["coffee"] -= BEVERAGE_MENU[coffee_choice]["coffee"]

    # a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0
    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

    print(f"Here is your latte 🍵 Enjoy!")


def start_machine():

    while machine_on:

        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice in BEVERAGE_MENU:
            if check_resources(coffee_choice):
                inserted = request_payment()
                if inserted > BEVERAGE_MENU[coffee_choice]['price']:
                    print(f"Your change is: ${inserted - BEVERAGE_MENU[coffee_choice]['price']:.2f}")
                    serve_beverage(coffee_choice)
                elif inserted == BEVERAGE_MENU[coffee_choice]['price']:
                    serve_beverage(coffee_choice)
                else:
                    print(f"Sorry that's not enough money. Money refunded.")
        # Turn off the Coffee Machine by entering “off” to the prompt.
        elif coffee_choice == "off":
            turn_machine_off()
        elif coffee_choice == "report":
            generate_report()


start_machine()
