from ConcreteObserver import *
from Subject import *

iphoneStock = IphoneStock()

user1 = EmailNotificationUser("user1@xyx.com")
user2 = EmailNotificationUser("user2@xyx.com")
user3 = MobileNotificationUser("9988776655")

iphoneStock.addUser(user1)
iphoneStock.addUser(user2)
iphoneStock.addUser(user3)

iphoneStock.addIphone(30)
iphoneStock.addIphone(100)
iphoneStock.addIphone(-130)
iphoneStock.addIphone(100)