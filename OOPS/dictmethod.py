class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("mohit",10)
print(p.__dict__)
