list_of_people = ['Marcus Aurelius', 'Theodore Roosevelt', 'Julius Caesar']
print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")
print(f"{list_of_people[2]}, would you like to eat some pasta?")

print(f"{list_of_people[2]} will not be able to come.")

list_of_people[2] = 'Socrates'
print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")
print(f"{list_of_people[2]}, would you like to eat some gyros?")