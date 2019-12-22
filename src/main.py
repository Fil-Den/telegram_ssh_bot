'''
Programm entry point.
Set log format,
parse config and run bot, also
set messages and commands handlers
'''
import json
import logging
import argparse
from bot import (
    TelegramBot, MsgHandler
)
from system import system
from configJsonSchema import CONFIG_JSON_SCHEMA
from jsonschema import (
    validate, ValidationError
)


def getPathToCfg():
    '''create argument parser and try get config path. If can't get
    return default value cfg.json. If user wait help message print it
    and exit program'''
    parser = argparse.ArgumentParser(
        description='Run "ssh" bot. Allows send cli commands in telegram ' +
                    'and seen standart output.')
    parser.add_argument(
        '-c', '--config', dest='config', type=str, nargs='?',
        help='contains path to config file (default cfg.json)',
        default='cfg.json'
    )
    args = parser.parse_args()
    return args.config


def runAllCommand(command):
    '''run command and return result'''
    return system.runCommand(command)


def main():
    '''programm entry point'''
    cfgPath = getPathToCfg()

    # set log output format in json
    logging.basicConfig(
        format='{ "time": "%(asctime)s",  "level": "%(levelname)s", ' +
               '"msg": "%(message)s" }', level=logging.INFO)

    # load and validate config
    with open(cfgPath) as file:
        cfg = json.load(file)
    try:
        validate(instance=cfg, schema=CONFIG_JSON_SCHEMA)
    except ValidationError:
        logging.error("config parse error! (See example in README).")
        return

    # run bot
    bot = TelegramBot(
        cfg['telegram']['api_token'],
        cfg['telegram']['proxy_url'],
        cfg['telegram']['proxy_username'],
        cfg['telegram']['proxy_password'])
    allowed_users = cfg['telegram']['allowed_users']
    # add msg handler
    if cfg['allow_all_commands']:
        bot.set_message_handler(
            MsgHandler(
                (lambda cmd: system.runCommand(cmd)),
                allowed_users=allowed_users
            )
        )
    # add commands
    for cmd in cfg['commands']:
        bot.set_command_handler(
            cmd['command_name'],
            MsgHandler(
                # (lambda cmd: system.runCommand('dir')),
                (lambda msg: system.runCommand(cmd['command'])),
                allowed_users=allowed_users
            )
        )
    bot.start_polling()


if __name__ == '__main__':
    main()
