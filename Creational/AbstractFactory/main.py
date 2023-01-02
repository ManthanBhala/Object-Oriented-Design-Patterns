from AbstractFactory import Playlist

playlist = Playlist()
songs = playlist.playSongs("party")
song = songs.playPartySongs("DopeShope")
song.play()