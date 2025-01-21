prompt="\nWhat topping would you like on your pizza?"
prompt+="\nEnter 'quit' if you no longer want to add more toppings:"

while True:
    topping=input(prompt)
    if topping != 'quit':
        print(f"{topping} is added unto your pizza.")
    else:
        break 