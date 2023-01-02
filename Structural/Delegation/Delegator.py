from Delegatee import *

class Game:
    def __init__(self):
        self.gameView = None
    
    def setGameView(self, gameView):
        if(gameView == "First Person"):
            self.gameView = FirstPersonView()
        else:
            self.gameView = ThirdPersonView()
        self.gameView.getView()