class ConversationHistory:

    def __init__(self):
        self.messages = []

    def add_message(self, msg):
        self.messages.append(msg)

    def get_all_messages(self):
        return self.messages