# Exercise 7-8: Deli
sandwich_orders = ['turkey', 'ham', 'tuna', 'meatball']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
