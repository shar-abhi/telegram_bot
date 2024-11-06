# Getting Started 

This is a repo for a Telegram chatbot which will answer queries using the llama3.2 LLM model

## Pre-requisites
- You will need to generate a token for the Telegram bot which will be used in your code to interact with the bot. Checkout [this link](https://core.telegram.org/bots/tutorial#obtain-your-bot-token)
- You will need the python-telegram-bot and ollama python packages for this to run properly. Following command can be used for this:-

```
pip3 install python-telegram-bot ollama
```



## Running the bot

- To run the code you can execute the command as follows

```
cd telebot_project; python3 new_bot.py --token <YOUR_BOT_TOKEN>
```

***Sample logs***
```
2024-11-06 22:34:06,754 - apscheduler.scheduler - INFO - Scheduler started
2024-11-06 22:34:06,755 - telegram.ext.Application - INFO - Application started
2024-11-06 22:34:56,930 - __main__ - INFO - Ollama will be responding
2024-11-06 22:35:09,123 - __main__ - INFO -
Bot Wrote:
==============
Telegram is a cloud-based messaging and voice/video calling app with end-to-end encryption, available for iOS, Android devices.

```

- Once running, from your Telegram app, type the command '/start' to start the converstation with the bot
- The LLM takes some time to initially generate a response and reply to the query.  
