class Employee:
    enmae = "Rajan"
    emplcount = 0

    def __init__(self,name = ""):
        self.name = name
        self.raise_amount = 0.2
        Employee.emplcount += 1

    def show(self):
        print(f"the Name of employee is {self.name} and count is {self.emplcount} the raise amount  is {self.raise_amount}")


emp1 = Employee()
emp1.name = "Mohit"
emp1.show()
emp1.enmae = "Deepak"
print(emp1.enmae)

emp2 = Employee()
emp2.name = "Mohit"
emp2.show()
print(emp2.enmae)

emp2 = Employee()
emp2.name = "Robib"
emp2.show()
print(emp2.enmae)