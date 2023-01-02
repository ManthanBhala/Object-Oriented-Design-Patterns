from Handler import LogProcessor


class InfoLogProcessor(LogProcessor):

    def __init__(self, nextLogProcessor):
        super().__init__(nextLogProcessor)
    
    def log(self, logLevel, message):
        if(logLevel == self.INFO):
            print("INFO: " + message)
        else:
            super().log(logLevel, message)


class DebugLogProcessor(LogProcessor):

    def __init__(self, nextLogProcessor):
        super().__init__(nextLogProcessor)
    
    def log(self, logLevel, message):
        if(logLevel == self.DEBUG):
            print("DEBUG: " + message)
        else:
            super().log(logLevel, message)


class ErrorLogProcessor(LogProcessor):

    def __init__(self, nextLogProcessor):
        super().__init__(nextLogProcessor)
    
    def log(self, logLevel, message):
        if(logLevel == self.ERROR):
            print("ERROR: " + message)
        else:
            super().log(logLevel, message)
