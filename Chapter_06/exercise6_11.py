# Exercise 6-11: Cities
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37400000,
        'fact': 'The capital of Japan'
    },
    'Paris': {
        'country': 'France',
        'population': 2140000,
        'fact': 'The capital of France'
    },
    'Mexico City': {
        'country': 'Mexico',
        'population': 8920000,
        'fact': 'The capital of Mexico'
    }
}
for city, info in cities.items():
    print(f"{city} is in {info['country']} and has a population of {info['population']}.")
    print(f"Interesting fact: {info['fact']}")