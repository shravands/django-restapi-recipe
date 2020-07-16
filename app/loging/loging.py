# chnage in the logging functionality for logging

from requestlogs.storages import LoggingStorage, logger
from rest_framework.exceptions import NotFound


class CustomLogger(LoggingStorage):
    """Change in the default behaviour of the loging package"""
    def __init__(self):
        self.value = "the value is being set from the custom functionality"
        
    def store(self, entry):
        logger.info(self.prepare(entry))
        raise NotFound(entry.data)