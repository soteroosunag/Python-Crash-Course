# Exercise 7-10: Dream Vacation
dream_vacation = {}
while True:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[name] = place
    continue_prompt = input("Would you like to let another person respond? (yes/no) ")
    if continue_prompt == 'no':
        break
print("\n--- Dream Vacation Results ---")
for name, place in dream_vacation.items():
    print(f"{name} would like to visit {place}.")
