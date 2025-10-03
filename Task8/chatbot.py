import random

def chatbot():
    print("🤖 Chatbot: Hello! I'm your internship chatbot. Type 'bye' to exit.\n")

    responses = {
        "hi": ["Hi there!", "Hello! How can I help you?", "Hey! 👋"],
        "hello": ["Hello! How's your day?", "Hi! What’s up?"],
        "how are you": ["I'm just code, but I'm doing great 😃", "All good here, thanks for asking!"],
        "name": ["I'm a simple Python chatbot.", "You can call me PyBot 🤖"],
        "help": [
            "I can chat with you. Try these:\n- hi\n- how are you\n- tell me a joke\n- about\n- bye"
        ],
        "about": ["I'm a rule-based chatbot created for the Python Internship."],
        "joke": [
            "Why do Python programmers wear glasses? Because they can't C 😆",
            "Debugging: Being the detective in a crime movie where you are also the murderer 🕵️‍♂️",
        ],
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! 👋 Have a great day.")
            break

        found = False
        for key in responses:
            if key in user_input:
                print("🤖 Chatbot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("🤖 Chatbot: Sorry, I don’t understand that. Type 'help' to see what I can do.")

if __name__ == "__main__":
    chatbot()
