# Exercise 4-12: More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
	print(food)

for food in friend_foods:
	print(food)