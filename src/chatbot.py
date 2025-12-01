from .sentiment_analyzer import analyze_message_sentiment

class Chatbot:

    def analyze_message(self, text):
        """Tier 2: Returns sentiment for a single message."""
        return analyze_message_sentiment(text)

    def respond(self, text):
        """Simple reply logic."""
        t = text.lower()

        if "sad" in t or "angry" in t or "bad" in t:
            return "I'm sorry you're feeling this way. Tell me more."
        elif "happy" in t or "good" in t or "great" in t:
            return "That's wonderful to hear!"
        else:
            return "I understand. How else can I help you?"