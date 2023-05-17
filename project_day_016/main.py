# Day 16 Project: OOP-type Coffee Maker Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Coffee Machine Program Requirements
coffeemaker = CoffeeMaker()
menu = Menu()
pay_system = MoneyMachine()
machine_on = True

while machine_on:
    choice = input(f" What would you like? ({menu.get_items()}): ")

    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        coffeemaker.report()
        pay_system.report()
    else:
        beverage = menu.find_drink(choice)
        if not beverage:
            continue
        else:
            if coffeemaker.is_resource_sufficient(beverage) and pay_system.make_payment(beverage.cost):
                coffeemaker.make_coffee(beverage)

