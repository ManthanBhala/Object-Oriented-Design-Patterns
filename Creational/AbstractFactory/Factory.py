from ConcreteProduct import *

class PartySongsFactory:

    def playPartySongs(self, input):
        if(input == "DopeShope"):
            return DopeShope()
        elif(input == "DaaruParty"):
            return DaaruParty()
        else:
            return None

class SadSongsFactory:

    def playSadSongs(self, input):
        if(input == "ChannaMereya"):
            return ChannaMereya()
        elif(input == "Galliyan"):
            return Galliyan()
        else:
            return None