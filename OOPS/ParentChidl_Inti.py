class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):

    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang


mohit = Employee("Mohit",107)
rohan = Programmer("Rohan",102,"JAVA")
print(mohit.name)
print(rohan.name)