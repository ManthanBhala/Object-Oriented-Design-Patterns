class IphoneStock:

    def __init__(self):
        self.users = []
        self.iphoneCount = 0
    
    def addUser(self, user):
        self.users.append(user)
    
    def removeUser(self, user):
        self.users.remove(user)
    
    def notifyUsers(self):
        for user in self.users:
            user.notify()
    
    def addIphone(self, count):
        if(self.iphoneCount == 0 and count > 0):
            self.notifyUsers()
        self.iphoneCount += count
    
    def getIphoneCount(self):
        return self.iphoneCount
