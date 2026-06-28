
def get_response(user_input):
    """
    Function to get a predefined response based on user input.
    Uses if-elif statements to match user input with responses.
    """
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot!"
    elif user_input == "help":
        return "I can respond to: hello, how are you, bye, what is your name"
    else:
        return "I don't understand that. Type 'help' for available commands."


def main():
    """
    Main function to run the chatbot loop.
    Continuously takes user input and provides responses.
    """
    print("=" * 40)
    print("Welcome to Simple Chatbot!")
    print("Type 'bye' to exit")
    print("=" * 40)
    print()
    
    # Loop to keep chatbot running
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to exit
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        
        # Get and display response
        response = get_response(user_input)
        print(f"Bot: {response}")
        print()


if __name__ == "__main__":
    main()
