import discord
import logging

from enum import Enum

# Rudimentary enumerated error types
class ErrorTypes(Enum):
    USER, RECOVERABLE, INTERNAL, STARTUP, FATAL = range(5)

class BotException(Exception):

    def __init__(self, error_type, error_subject, error_details, *args):
        self.error_type = error_type
        self.error_subject = str(error_subject)
        self.error_details = str(error_details)
        self.error_other = args
        other_details = ''
        for detail in args:
            other_details += '{}\n'.format(detail)
        self.error_message = "`{subject} error: {details}`\n{others}".format(
                subject = self.error_type,
                details = self.error_details,
                others = other_details)

        logging.error(self.error_message)

        # If non-recoverable, quit
        if error_type >= ErrorTypes.STARTUP:
            os.exit()
            
    def __str__(self):
        return self.error_message
