# Exercise 8-10: Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = ["Hello World", "Hello, Computer!", "Wow! You can talk to me?"]
sent_messages = []
send_messages(messages, sent_messages)
print('Messages: ', messages)
print('Sent Messages: ', sent_messages)
