# Exercise 7-4: Pizza Toppings
prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you are finished. "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
