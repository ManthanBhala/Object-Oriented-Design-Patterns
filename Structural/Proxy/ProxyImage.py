from Image import EmployeeDatabaseImage
from RealImage import RealEmployeeDatabaseImage

class ProxyEmployeeDatabaseImage(EmployeeDatabaseImage):

    def __init__(self):
        super().__init__()
        self.realEmployeeDatabaseImage = RealEmployeeDatabaseImage()

    def create(self, client, employee):
        if(client.value == "ADMIN" or client.value == "USER"):
            self.realEmployeeDatabaseImage.create(client, employee)
            print("Created " + employee)
        else:
            print("Client not allowed")
    
    def delete(self, client, employee):
        if(client.value == "ADMIN"):
            self.realEmployeeDatabaseImage.delete(client, employee)
            print("Deleted " + employee)
        else:
            print("Client not allowed")