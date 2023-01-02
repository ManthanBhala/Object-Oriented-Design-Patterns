from AbstractObject import Employee

class Director(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getName(self):
        return super().getName()

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getName(self):
        return super().getName()