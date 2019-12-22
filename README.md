Telegram bot for control your remote server
===

This telegram bot is intendended for administrating your operating   
system. Server accept CLI commands in message and return standart   
output in answer message.

In Windows systems run commands with cmd.
In Linux systems run commands with standart command interpreter.


Requirements
---
Work only in python 3.
Another requirements in requirements.txt.


Structure
---

Project consist of 5 elements:
- main.py - getting parameters from config file, set all configs and run bot.
- configJsonSchema.py - contains json schema for configuration file.
- bot - packet, contains Bot class being a [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)   
library small wrapper, and contains message handler wrapper.
- system - contains clases for work with current operation system.
- config.json - contains all bot configurations


Usage
---
If you need a help, run script with -h parameter. And you will see    
something like:

```output
usage: main.py [-h] [-c [CONFIG]]

Run "ssh" bot. Allows send cli commands in telegram and seen standart output.

optional arguments:
  -h, --help            show this help message and exit
  -c [CONFIG], --config [CONFIG]
                        contains path to config file (default cfg.json)
```
