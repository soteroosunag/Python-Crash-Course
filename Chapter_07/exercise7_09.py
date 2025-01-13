# Exercise 7-9: No Pastrami
sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'tuna', 'pastrami', 'meatball']
finished_sandwiches = []
print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
