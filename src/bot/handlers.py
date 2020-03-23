'''Contains handler for processing messages.'''


class MsgHandler:
    '''Processing commands and messages from telegram.'''

    MAX_MESSAGE_SIZE = 4096
    RESTRICTED_MSG = "Access not allowed"

    def __init__(self, commandFunc, allowed_users=None):
        '''Add command for process.
        If allowed_users=None, then all users allowed.'''
        self._commandFunc = commandFunc
        self._allowedUsers = allowed_users

    def __call__(self, update, context):
        '''Command handler.'''
        if (self._allowedUsers and
                update.message.from_user.id not in self._allowedUsers):
            context.bot.send_message(
                chat_id=update.message.chat_id,
                text=self.RESTRICTED_MSG
            )
            return
        answer = self._commandFunc(update.message.text)
        answers = [answer[i:i+self.MAX_MESSAGE_SIZE]
                   for i in range(0, len(answer), self.MAX_MESSAGE_SIZE)]
        for ans in answers:
            context.bot.send_message(
                chat_id=update.message.chat_id,
                text=ans
            )
