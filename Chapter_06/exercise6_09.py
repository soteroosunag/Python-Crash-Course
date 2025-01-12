# Exercise 6-9: Favorite Places
favorite_places = {
    'John': ['Paris', 'Tokyo', 'New York'],
    'Jane': ['London', 'Sydney', 'Berlin'],
    'Alice': ['San Francisco', 'Barcelona', 'Rome']
}
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")