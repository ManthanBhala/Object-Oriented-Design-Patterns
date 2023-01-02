from RealObject import *
from NullObject import NullEmployee

class EmployeeFactory:
    def createEmployee(self, name, designation):
        if(designation == "Director"):
            return Director(name)
        elif(designation == "Developer"):
            return Developer(name)
        else:
            return NullEmployee(name)