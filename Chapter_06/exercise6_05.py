# Exercise 6-5: Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
