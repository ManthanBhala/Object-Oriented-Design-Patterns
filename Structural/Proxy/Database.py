class EmployeeDatabase:

    def __init__(self):
        self.employees = []

    def create(self, employee):
        self.employees.append(employee)

    def delete(self, employee):
        self.employees.remove(employee)