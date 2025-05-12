#Import the Open AI SDK
from openai import OpenAI

#Import the os and dotenv libraries to keep the API key a secrete
import os
from dotenv import load_dotenv

#Import the sys library to pass propmts through the command line
#This mans we don' have to rewrite this file to update the prompt every time
import sys

load_dotenv()

#The API key is in a file called .env
#The file contains a line DEEPSEEK_API_KEY=<API key value>
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

#sys.argv[0] is the actual script, sys.argv[1] is the first arg passed on the CLI
#This means we can call the module in a terminal and pass it a string argument for the prompt
if len(sys.argv) == 2:
    PROMPT = sys.argv[1]

    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url='https://api.deepseek.com')

    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'system', 'content': 'You are a helpful AI assistant'},
            {'role': 'user', 'content': PROMPT},
            ],
        stream=False
)        

    print(response.choices[0].message.content)

if __name__ == '__main__':
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url='https://api.deepseek.com')
    print('Enter your prompt:')
    INPUT = input()
    messages= [{'role': 'system', 'content': 'You are a helpful AI assistant'}]
    while INPUT != '/bye':
        messages.append({'role': 'user', 'content': INPUT})
        response = client.chat.completions.create(
                model='deepseek-chat',
                messages=messages
                )
        messages.append(response.choices[0].message)
        print(response.choices[0].message.content)
        print('>>>', end='')
        INPUT = input()
