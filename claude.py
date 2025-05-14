import anthropic

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ANTHROPIC_API_KEY')

class Chatbot:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.messages = []

    def talk(self, message):
        self.messages.append({
            'role': 'user',
            'content':[
                {
                    'type': 'text',
                    'text': message 
                    }
                ]
            }
        )
        response = self.client.messages.create(
            model='claude-3-7-sonnet-20250219',
            max_tokens=1000,
            temperature=1,
            system='You are a helpful AI assisant.',
            messages=self.messages
            )
        response_text = response.content[0].text
 
        print(response_text)
        self.messages.append({
            'role': 'assistant',
            'content': response_text
        })

def main():
    chatbot = Chatbot()
    print('Please enter a prompt below, or enter /bye to quit')
    message = input('>>> ')
    while message != '/bye':
        chatbot.talk(message)
        message = input('>>> ')


if __name__ == '__main__':
    main()
