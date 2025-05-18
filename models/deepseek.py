#Import the Open AI SDK
from openai import OpenAI

#Import the os and dotenv libraries to keep the API key a secrete
import os
from dotenv import load_dotenv

from config import SYSTEM_PROMPT

load_dotenv()

#The API key is in a file called .env
#The file contains a line DEEPSEEK_API_KEY=<API key value>
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

class DeepSeek:

    def __init__(self):
        self.client = OpenAI(
                api_key=DEEPSEEK_API_KEY,
                base_url='https://api.deepseek.com'
                )

        self.messages = [{
            'role': 'system',
            'content': SYSTEM_PROMPT
            }]

    """
    Takes as input a message from the user, appends it to the current conversation
    gets a response from the AI API, prints it to the standard output and saves
    that message to keep the conversation flowing
    """
    def talk(self, message):
        self.messages.append({
            'role': 'user',
            'content': message
            })

        response = self.client.chat.completions.create(
                model='deepseek-chat',
                messages=self.messages
                )

        self.messages.append(response.choices[0].message)
        print('# ' + response.choices[0].message.content)

def main():
    chatbot = DeepSeek()
    print('Enter your prompt below, or use /bye to quit')
    message = input('>>> ')
    while message != '/bye':
       chatbot.talk(message)
       message = input('>>> ')

if __name__ == '__main__':
    main()
