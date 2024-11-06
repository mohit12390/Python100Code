class Employee:

    def __init__(self):
        self.no_of_employee = 0
        self.employee  = []


    def add_employee(self,employee):
        self.employee.append(employee)
        self.no_of_employee = len(self.employee)

    def show_employee(self):
        print(f"The employee count is {self.no_of_employee} and name of employee is {self.employee}")


emp1 = Employee()

list_employee = ["Mohit","Rajesh","Dinakr"]
emp1.add_employee(list_employee)
emp1.show_employee()