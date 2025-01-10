# Exercise 5-2: More Conditional Tests
test_string = 'hello'
print(test_string == 'hello')
print(test_string == 'Hello')
print(test_string.lower() == 'hello')
print(test_string.lower() == 'goodbye')

test_number = 10
print(test_number == 10)
print(test_number == 11)
print(test_number > 9)
print(test_number < 11)
print(test_number >= 10)
print(test_number <= 10)
print(test_number != 10)
print(test_number > 9 and test_number < 11)
print(test_number > 0 or test_number < 0)

test_list = [1, 2, 3, 4, 5]
print(1 in test_list)
print(6 in test_list)
print(1 not in test_list)
print(6 not in test_list)