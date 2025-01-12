# Exercise 6-8: Pets
firulais = {
    'name': 'Firulais',
    'animal_type': 'dog',
    'owner_name': 'John Doe'
}
worlock = {
    'name': 'Worlock',
    'animal_type': 'cat',
    'owner_name': 'Jane Smith'
}
manny = {
    'name': 'Manny',
    'animal_type': 'hamster',
    'owner_name': 'Alice Johnson'
}
pets = [firulais, worlock, manny]
for pet in pets:
    print(pet['name'])
    print(pet['animal_type'])
    print(pet['owner_name'])