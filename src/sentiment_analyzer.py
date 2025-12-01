from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_message_sentiment(text):
    """Tier 2: Sentiment for a single user message."""
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.3:
        return "Positive"
    elif score <= -0.3:
        return "Negative"
    return "Neutral"


def analyze_overall_sentiment(messages):
    """Tier 1: Overall conversation sentiment."""
    if not messages:
        return "Neutral (no messages)"

    total = 0
    for m in messages:
        total += analyzer.polarity_scores(m)["compound"]

    avg = total / len(messages)

    if avg >= 0.3:
        return "Positive – user generally satisfied"
    elif avg <= -0.3:
        return "Negative – general dissatisfaction"
    else:
        return "Neutral – mixed mood"
