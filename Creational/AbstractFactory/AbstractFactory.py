from Factory import *

class Playlist:
    
    def playSongs(self, input):
        if(input == "party"):
            return PartySongsFactory()
        elif(input == "sad"):
            return SadSongsFactory()
        else:
            return None