from DelegationInterface import GameView

class FirstPersonView(GameView):
    def __init__(self):
        super().__init__()
    
    def getView(self):
        print("First Person View Set")

class ThirdPersonView(GameView):
    def __init__(self):
        super().__init__()
    
    def getView(self):
        print("Third Person View Set")