from src.chatbot import Chatbot
from src.conversation import ConversationHistory
from src.sentiment_analyzer import analyze_overall_sentiment

def main():
    chatbot = Chatbot()
    history = ConversationHistory()

    print("Chatbot: Hello! I'm here to chat with you. Type 'exit' to finish.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # Tier 2: Message-level sentiment
        sentiment = chatbot.analyze_message(user_input)
        print(f"→ Sentiment: {sentiment}")

        # Save to conversation (Tier 1)
        history.add_message(user_input)

        # Chatbot reply
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        print()

    # Tier 1: Conversation-level sentiment
    overall = analyze_overall_sentiment(history.get_all_messages())
    print("\nFinal Output:")
    print("Overall conversation sentiment:", overall)

if __name__ == "__main__":
    main()
