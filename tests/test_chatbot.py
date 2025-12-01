from src.chatbot import Chatbot

def test_bot_response():
    bot = Chatbot()
    resp = bot.respond("I am sad")
    assert "sorry" in resp.lower()