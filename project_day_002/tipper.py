print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? "))
tip_rate = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
people_total = int(input("How many people to split the bill? "))

split_cost = round(((bill_total * (1 + tip_rate / 100)) / people_total), 2)

print(f"Each person should pay: ${split_cost:.2f}")
