class School:

    def __init__(self):
        self.name = ""
        self.age = 0

    def hello(self):
        print(self.name)
        print(self.age)


print(School.hello("Rajan"))