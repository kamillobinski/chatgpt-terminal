import os
from revChatGPT.ChatGPT import Chatbot


class OpenAI:

    def __init__(self):
        self.conversation_id = None
        self.chatbot = Chatbot({
            "session_token": os.environ['AI_SESSION_TOKEN']
        }, conversation_id=None, parent_id=None)

    def ask(self, message: str):
        response = self.chatbot.ask(
            message, conversation_id=self.conversation_id, parent_id=None)
        self.conversation_id = response['conversation_id']
        return Response(response)


class Response():

    def __init__(self, response: dict):
        self.message = response['message'].replace('\n', ' ')
        self.message_raw = response['message']
        self.conversation_id = response['conversation_id']
        self.parent_id = response['parent_id']
