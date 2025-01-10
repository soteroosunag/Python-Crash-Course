# Exercise 4-10: Slices
cubes = [x**3 for x in range(1,11)]
for cube in cubes:
	print(cube)
	
print(f'The first three items in the list are: {cubes[:3]}')
print(f'The middle three items in the list are: {cubes[4:7]}')
print(f'The last three items in the list are: {cubes[-3:]}')