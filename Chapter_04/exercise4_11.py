# Exercise 4-11: My Pizzas, Your Pizzas
pizzas = ['Meat Lovers', 'Extra Cheese', 'Pepperoni']
friend_pizzas = pizzas[:]

pizzas.append('BBQ Chicken')
friend_pizzas.append('Hawaiian')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)