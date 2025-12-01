from src.sentiment_analyzer import analyze_message_sentiment

def test_positive():
    assert analyze_message_sentiment("I feel great!") == "Positive"

def test_negative():
    assert analyze_message_sentiment("This is terrible") == "Negative"