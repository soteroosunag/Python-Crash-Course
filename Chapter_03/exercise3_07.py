list_of_people = ['Marcus Aurelius', 'Theodore Roosevelt', 'Julius Caesar']
print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")
print(f"{list_of_people[2]}, would you like to eat some pasta?")

print(f"{list_of_people[2]} will not be able to come.")

list_of_people[2] = 'Socrates'
print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")
print(f"{list_of_people[2]}, would you like to eat some gyros?")

print("We found a bigger table!")

list_of_people.insert(0, 'Plato')
list_of_people.insert(2, 'Aristotle')
list_of_people.append('Epicurus')

print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")
print(f"{list_of_people[2]}, would you like to eat some gyros?")
print(f"{list_of_people[3]}, would you like to eat some gyros?")
print(f"{list_of_people[4]}, would you like to eat some gyros?")
print(f"{list_of_people[5]}, would you like to eat some gyros?")

print("We found a smaller table!")

sorry_person = list_of_people.pop()
print(f"Sorry, {sorry_person}, we don't have a table for you.")

sorry_person = list_of_people.pop()
print(f"Sorry, {sorry_person}, we don't have a table for you.")

sorry_person = list_of_people.pop()
print(f"Sorry, {sorry_person}, we don't have a table for you.")

sorry_person = list_of_people.pop()
print(f"Sorry, {sorry_person}, we don't have a table for you.")

print(f"{list_of_people[0]}, would you like to eat some pizza?")
print(f"{list_of_people[1]}, would you like to eat some burgers?")