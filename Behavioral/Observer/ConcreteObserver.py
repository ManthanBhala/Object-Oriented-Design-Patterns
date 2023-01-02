from Observer import NotificationUser


class EmailNotificationUser(NotificationUser):

    def __init__(self, emailId):
        super().__init__()
        self.emailId = emailId
    
    def notify(self):
        print("Email Sent to " + self.emailId + ": Iphone currently in stock")


class MobileNotificationUser(NotificationUser):

    def __init__(self, mobileNo):
        super().__init__()
        self.mobileNo = mobileNo
    
    def notify(self):
        print("Message Sent to " + self.mobileNo + ": Iphone currently in stock")