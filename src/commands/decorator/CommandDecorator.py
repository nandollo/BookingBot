from .HandlerDecorator import HandlerDecorator
from telegram import Update, Message


class CommandDecorator(HandlerDecorator):

    def check_update(self, update: Update):
        result = False
        if isinstance(update, Update) and (update.message or update.edited_message):
            new_update = self.copy_update(update)
            message = new_update.message or new_update.edited_message  # type: Message
            if message.text.startswith('/'):
                message.text = message.text[1:]
                result = super().check_update(new_update)
        return result