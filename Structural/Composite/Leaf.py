from Interface import FileSystem

class File(FileSystem):

    def __init__(self, fileName):
        self.fileName = fileName

    def ls(self):
        print("file name " + self.fileName)
