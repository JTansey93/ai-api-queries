#Anthropic SDK
import anthropic

#Use os and dotenv to get the API key`
import os
from dotenv import load_dotenv

from config import SYSTEM_PROMPT

load_dotenv()
API_KEY = os.getenv('ANTHROPIC_API_KEY')

class Claude: 
    def __init__(self):
        #Initialise client and store messages to allow a continual chat
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.messages = []

    """
    Takes as input a message from the user, appends it to the current conversation
    gets a response from the AI API, prints it to the standard output and saves
    that message to keep the conversation flowing

    TODO: Implement some kind of logging
    """
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
            system=SYSTEM_PROMPT,
            messages=self.messages
            )
        response_text = response.content[0].text
 
        print('# ' + response_text)
        self.messages.append({
            'role': 'assistant',
            'content': response_text
        })

def main():
    chatbot = Claude()
    print('Please enter a prompt below, or enter /bye to quit')
    message = input('>>> ')
    while message != '/bye':
        chatbot.talk(message)
        message = input('>>> ')


if __name__ == '__main__':
    main()
