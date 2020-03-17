### Notification bot for twitter using Telegram

Requirements:
```console
$ pip install pyTelegramBotAPI
```

Step-by-step Guide for bot

- Download and install Telegram application to your smart phone.
- Search for @BotFather and type /start
- Type /newbot and follow insturctions. And then, your bot token is created. Keep that token secretly.

Now our Telegram bot is ready. Its time to follow some twitter pages and get notifications from telegram.

- Run initialize.py with your input parameters such as followlist
- Edit main.py to change Telegram bot token and Telegram user id
- Run main.py using crontab

**That code will open crontab console**
```console
$ sudo nano /etc/crontab
```
**Insert code below into the console**
```console
* * * * * root python main.py
```

Now, we can wait for new messages about pages we want to follow on twitter.

