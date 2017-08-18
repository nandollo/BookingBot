import copy
from telegram import Bot, Update
from commands import AbstractBookingHandler


class HandlerDecorator(AbstractBookingHandler):

    def __init__(self, command: AbstractBookingHandler):
        super(HandlerDecorator, self).__init__(command.backend)
        self._command = command

    def check_update(self, update):
        return self._command.check_update(update)

    def execute(self, bot: Bot, update: Update):
        self._command.execute(bot, update)

    def copy_update(self, update: Update) -> Update:
        """
        Creates a shallow copy of the Update object, only the text of the message will be deep copied.
        :param update: The update that will be copied.
        :return: The shallow copy of the provided object.
        """
        new_update = copy.copy(update)
        if update.message:
            new_update.message = copy.copy(update.message)
            new_update.message.text = copy.deepcopy(update.message.text)
        elif update.edited_message:
            new_update.edited_message = copy.copy(update.edited_message)
            new_update.edited_message.text = copy.deepcopy(update.edited_message.text)
        return new_update



