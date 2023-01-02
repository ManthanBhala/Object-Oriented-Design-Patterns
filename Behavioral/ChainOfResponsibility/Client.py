from ConcreteHandler import *

class Logger:

    def __init__(self):
        self.logger = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))
    
    def logMessage(self, logLevel, message):
        self.logger.log(logLevel, message)