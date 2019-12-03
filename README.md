Telegram bot for controle your remote server
===

This telegram bot is intendended for administrating your operating   
system. Server accept CLI commands in messages and return standart   
output in answer message.   


Structure
---

Project consist of 4 files:
- main.py - contains programm entry point, getting parameters from   
config file
- bot.py - contains Bot class being a [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)   
library small wrapper
- system.py - contains System class being a operation system   
abstraction
- config.json - contains all bot configurations


Usage
---
You need write all configs and run script simply.
```cmd
python main.py
```
