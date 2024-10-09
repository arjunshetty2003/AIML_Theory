def get_response(user_input) :

    response = {
        "hi" : "Hi, how are you",
        "how are you?" : "Thanks for asking but I don't have any feelings",
        "what is your name?" : "I'm just a simple rule-based chatbot",
        "bye" : "Goodbye! Have a great day!",
        "help": "Sure! You can ask me about my features or any other questions.",
        }
    
    if user_input not in response.keys() :
        return "Sorry, I can't understand what are you trying to say"
    
    return response[user_input]

def main() :

    print("Enter your queries")
    while True :
        user_input = input("You: ").lower()
        print(get_response(user_input))

        if user_input == "bye" :
            print("Chatbot: ", get_response(user_input))
            break

if __name__ == "__main__" :
    main()


