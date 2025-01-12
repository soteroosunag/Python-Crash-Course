# Exercise 6-6: Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['john', 'sarah', 'jen', 'michael', 'oscar']

for person in people:
    if person in favorite_languages.keys():
        print(f'{person.title()}, thank you for taking the poll.')
    else:
        print(f'{person.title()}, please take the poll.')
