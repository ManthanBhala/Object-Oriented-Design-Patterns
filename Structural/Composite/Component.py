from Interface import FileSystem

class Directory(FileSystem):

    def __init__(self, directoryName):
        self.directoryName = directoryName
        self.fileSystemList = []

    def add(self, fileSystemObj):
        self.fileSystemList.append(fileSystemObj)

    def ls(self):
        print("Directory name " + self.directoryName)
        for fileSystemObj in self.fileSystemList:
            fileSystemObj.ls()
