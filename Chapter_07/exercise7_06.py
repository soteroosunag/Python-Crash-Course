# Exercise 7-6: Three Exits
prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when you are finished. "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        continue
    elif int(age) < 3:
        print("Your ticket is free.")
    elif int(age) < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
