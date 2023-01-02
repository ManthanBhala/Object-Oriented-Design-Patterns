class LogProcessor:

    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, nextLogProcessor):
        self.nextLogProcessor = nextLogProcessor
    
    def log(self, logLevel, message):
        if(self.nextLogProcessor != None):
            self.nextLogProcessor.log(logLevel, message)