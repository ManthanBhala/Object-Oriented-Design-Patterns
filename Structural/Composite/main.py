from Component import Directory
from Leaf import File

movieDirectory = Directory("Movie")

border = File("Border")
movieDirectory.add(border)

comedyMovieDirectory = Directory("ComedyMovie")
hulchul = File("Hulchul")
comedyMovieDirectory.add(hulchul)
movieDirectory.add(comedyMovieDirectory)

movieDirectory.ls()
