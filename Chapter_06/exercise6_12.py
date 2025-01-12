# Exercise 6-12: Extensions
glossary = {
    'variable': 'A name that refers to a value stored in memory.',
    'boolean': 'A value that is either True or False',
    'loop': ['A block of code that is repeated until a condition is met.', 'A shape produced by a curve that returns to its starting point.'],
    'list': 'A collection of items in a sequence.',
    'dictionary': ['A collection of key-value pairs.', 'A book of words and their definitions.']
}
for term, definition in glossary.items():
    if isinstance(definition, list):
        print(f'{term}:')
        for item in definition:
            print(f'- {item}')
    else:
        print(f'{term}: {definition}')
    print('\n') 