class Person:
    name = "Mohit Gangil"
    occupation = "Lead Engineer"
    salary = 150000

    def info(self):
        print(f"{self.name} {self.occupation}")

    def __init__(self):
        print("You are inside constructor")
        pass

# calling constructor
a = Person()
# set method
a.name = "Mohit Gupta"
a.occupation = "Lead Developer"
a.salary = 15000000
print(f"Tha Name is : {a.name} \nOccupation are :  {a.occupation} \nsalary is : {a.salary}")
# method call
a.info()