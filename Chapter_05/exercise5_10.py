# Exercise 5-10: Checking Usernames
current_users = ['admin', 'john', 'jane', 'alice', 'bob']
current_users_lower = [user.lower() for user in current_users]
new_users = ['JOHN', 'travis', 'kevin', 'ross', 'Alice']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken.")
    else:
        print(f"Congratulations, {new_user} is available.")
