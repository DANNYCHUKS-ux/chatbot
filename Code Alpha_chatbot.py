
def chatbot():
    print("Welcome to Basic Chatbot!")
    print("Type 'hello', 'how are you', or 'bye' to chat.")
    print("You can also type 'exit' to close the chatbot.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")

        elif user_input == "exit":
            print("Bot: Chatbot closed. Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that message.")


chatbot()
