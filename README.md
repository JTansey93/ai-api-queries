This project uses uv for dependency management.

You can run the DeepSeek API query by running
```bash
uv run deepseek.py
```

The API key is stored in the .env file and loaded with python-dotenv as 'DEEPSEEK_API_KEY'

At the moment this just gives a cli to talk to deepseek-v3

TODO:
Add functionality for other LLM APIs
