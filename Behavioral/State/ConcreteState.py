from State import MobileState


class GeneralMode(MobileState):

    def __init__(self, mobile):
        super().__init__()
        self.mobile = mobile
    
    def toGeneral(self):
        print("Already in General Mode")
    
    def toVibrate(self):
        print("Switched to Vibrate Mode")
    
    def toSilent(self):
        print("Switched to Silent Mode")


class VibrateMode(MobileState):

    def __init__(self, mobile):
        super().__init__()
        self.mobile = mobile
    
    def toGeneral(self):
        print("Switched to General Mode")
    
    def toVibrate(self):
        print("Already in Vibrate Mode")
    
    def toSilent(self):
        print("Switched to Silent Mode")


class SilentMode(MobileState):

    def __init__(self, mobile):
        super().__init__()
        self.mobile = mobile
    
    def toGeneral(self):
        print("Switched to General Mode")
    
    def toVibrate(self):
        print("Switched to Vibrate Mode")
    
    def toSilent(self):
        print("Already in Silent Mode")