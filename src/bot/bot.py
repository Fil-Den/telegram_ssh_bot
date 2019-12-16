'''realize api for bot working'''
import logging
from telegram.ext import (
    Updater, CommandHandler,
    MessageHandler, Filters
)


class TelegramBot:
    '''class for work with telegram'''
    def __init__(self, token, proxy_url,
                 username=None, passord=None, connection_timeout=7):
        '''initialize variables'''
        if proxy_url:
            request_kwargs = {
                'proxy_url': proxy_url,
                'connect_timeout': connection_timeout
            }
            if username:
                request_kwargs['urllib3_proxy_kwargs'] = {
                    'username': username,
                    'password': passord
                }
            self._updater = Updater(token=token, request_kwargs=request_kwargs,
                                    use_context=True)
        else:
            self._updater = Updater(token=token, use_context=True)

    def set_command_handler(self, command, handler):
        '''set command handler function'''
        cmd_handler = CommandHandler(command, handler)
        self._updater.dispatcher.add_handler(cmd_handler)

    def set_message_handler(self, msg_handler):
        '''set start_handler function on messages'''
        echo_handler = MessageHandler(Filters.text, msg_handler)
        self._updater.dispatcher.add_handler(echo_handler)

    def start_polling(self):
        '''start pooling on updater and lock process'''
        self._updater.start_polling(bootstrap_retries=5)
        logging.info("Bot started!")
        self._updater.idle()
