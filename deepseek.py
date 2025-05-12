#Import the Open AI SDK
from openai import OpenAI

#Import the os and dotenv libraries to keep the API key a secrete
import os
from dotenv import load_dotenv

load_dotenv()

#The API key is in a file called .env
#The file contains a line DEEPSEEK_API_KEY=<API key value>
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

if __name__ == '__main__':
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url='https://api.deepseek.com')

    print('Enter your prompt and hit enter below, or use /bye and hit enter to quit.')
    INPUT = input('>>>')

    #TODO: Think of a better way to let the user edit the system prompt
    messages= [{'role': 'system', 'content': 'You are a helpful AI assistant'}]

    while INPUT != '/bye':
        messages.append({'role': 'user', 'content': INPUT})
        response = client.chat.completions.create(
                model='deepseek-chat',
                messages=messages
                )
        messages.append(response.choices[0].message)
        print(response.choices[0].message.content)
        INPUT = input('>>>')
