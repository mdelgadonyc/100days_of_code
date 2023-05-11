# Day 10 Project: Calculated fun!

from art import logo

#Add
def add(n1, n2):
    return n1 + n2


#Substract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))

    for op in operations:
        print(op)

    while (1):
        operation_symbol = input("Pick an operation: ")

        function = operations[operation_symbol]

        num2 = float(input("What's the next number?: "))

        result = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        resp = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )

        if resp == 'n':
            calculator()

        num1 = result


calculator()
