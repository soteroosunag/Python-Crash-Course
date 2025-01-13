# Exercise 7-5: Movie Tickets
prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is free.")
    elif int(age) < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
