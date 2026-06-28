print("Welcome to Simple ChatBot")

while True:
    message = input("You: ")
    message = message.lower()

    if message == "hi":
        print("Bot: Hello!")
    elif message == "hello":
        print("Bot: Hi! Nice to meet you.")
    elif message == "how are you":
        print("Bot: I am doing well. Thanks for asking.")
    elif message == "what is your name":
        print("Bot: My name is ChatBot.")
    elif message == "who made you":
        print("Bot: I was made using Python.")
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")