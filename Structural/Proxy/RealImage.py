from Image import EmployeeDatabaseImage
from Database import EmployeeDatabase

class RealEmployeeDatabaseImage(EmployeeDatabaseImage):

    def __init__(self):
        super().__init__()
        self.employeeDatabase = EmployeeDatabase()

    def create(self, client, employee):
        self.employeeDatabase.create(employee)
    
    def delete(self, client, employee):
        self.employeeDatabase.delete(employee)