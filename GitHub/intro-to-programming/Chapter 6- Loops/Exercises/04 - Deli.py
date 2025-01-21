sandwich_orders = ["Grilled Cheese Sandwich", "Chicken Sandwich", "Falafel Sandwich", "Tuna Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich} is still being made.")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} is ready.")
