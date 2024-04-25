import random

# Define some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
    "what's your name": ["I'm a chatbot ", "You can call me chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?", "I didn't quite catch that."],
}

# Function to get response
def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
