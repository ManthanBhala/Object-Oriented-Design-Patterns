from ProxyImage import ProxyEmployeeDatabaseImage
from Client import Client

employeeDatabase = ProxyEmployeeDatabaseImage()

client1 = Client.ADMIN
client2 = Client.USER
client3 = Client.USER

employeeDatabase.create(client1, "Raju")
employeeDatabase.create(client2, "Deepak")
employeeDatabase.create(client3, "Jai")
employeeDatabase.delete(client2, "Deepak")
employeeDatabase.delete(client1, "Deepak")
