sandwich_orders = [
    "Grilled Cheese Sandwich", "Pastrami Sandwich", "Chicken Sandwich",
    "Pastrami Sandwich", "Falafel Sandwich", "Pastrami Sandwich", "Tuna Sandwich"]
finished_sandwiches = []

print("Sorry, there are no more pastramis left.")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

print("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich} is still being made.")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} is ready.")