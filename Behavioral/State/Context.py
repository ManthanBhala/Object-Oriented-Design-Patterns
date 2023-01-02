from ConcreteState import SilentMode, GeneralMode, VibrateMode

class Mobile:

    def __init__(self):
        self.generalMode = GeneralMode(self)
        self.vibrateMode = VibrateMode(self)
        self.silentMode = SilentMode(self)
        self.mode = self.generalMode
    
    def turnGeneralMode(self):
        self.mode.toGeneral()
        self.mode = self.generalMode
    
    def turnVibrateMode(self):
        self.mode.toVibrate()
        self.mode = self.vibrateMode
    
    def turnSilentMode(self):
        self.mode.toSilent()
        self.mode = self.silentMode