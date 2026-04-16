print("Simple AI Chatbot")
print("Type 'bye' to exit")

while True:
    msg = input("You: ").lower()

    if msg == "hello":
        print("Bot: Hi! Nice to meet you.")
    elif msg == "how are you":
        print("Bot: I am fine, thank you.")
    elif msg == "what is your name":
        print("Bot: I am a simple AI chatbot.")
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")