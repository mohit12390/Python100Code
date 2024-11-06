class Person:

    def __init__(self,Name , occupation, salary):
        self.Name = Name
        self.occupation = occupation
        self.salary = salary

    def display(self):
        print(f"{self.Name} is an {self.occupation} with salary  {self.salary}")


person1 = Person("Mohit","Consultant",120000)
person1.display()
