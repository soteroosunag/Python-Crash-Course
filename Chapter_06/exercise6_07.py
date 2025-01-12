# Exercise 6-7: People
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}
other_person = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}
another_person = {  
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Chicago'
}
people = [person, other_person, another_person]
for person in people:
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])