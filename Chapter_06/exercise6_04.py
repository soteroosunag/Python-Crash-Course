# Exercise 6-4: Glossary 2
glossary = {
    'variable': 'A name that refers to a value stored in memory.',
    'boolean': 'A value that is either True or False',
    'loop': 'A block of code that is repeated until a condition is met.',
    'list': 'A collection of items in a sequence.',
    'dictionary': 'A collection of key-value pairs.'
}
for word, definition in glossary.items():
    print(f'A {word} is: {definition.lower()}\n')
