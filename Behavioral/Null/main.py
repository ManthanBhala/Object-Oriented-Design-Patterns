from Client import EmployeeFactory

employeeFactory = EmployeeFactory()
print(employeeFactory.createEmployee("Manoj", "Developer").getName())
print(employeeFactory.createEmployee("Ram", "Manager").getName())