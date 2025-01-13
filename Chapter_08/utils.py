def hello_world():
    print("Hello World")

def show_message(message):
    print(message)

def greatest_common_divisor(x, y):
    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x % y)