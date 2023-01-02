from AbstractObject import Employee

class NullEmployee(Employee):
    def getName(self):
        return "Not available"