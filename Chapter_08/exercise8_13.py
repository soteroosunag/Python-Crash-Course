# Exercise 8-13: User Profile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('sotero', 'osuna', field='computer science', favorite_language='python', favorite_subfield='ai/ml')
print(user_profile)