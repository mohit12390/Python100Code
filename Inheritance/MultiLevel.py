class Human:

    def __init__(self,name,eat,walk):
        self.eat = eat
        self.name = name
        self.walk = walk

class Developer(Human):

    def __init__(self,name,eat,walk,coding):
        super().__init__(name,eat,walk)
        self.coding = coding

    def coding(self):
        print("This is my coding stuff")

class Programmer(Developer):

    def __init__(self,name,eat,walk,coding,programming):
        super().__init__(name,eat,walk,coding)
        self.programming = programming

    def programming(self):
        print("I am a programmer")


prg = Programmer("Programmer","pava","yes","C++","JAVA")
print(prg.name)
print(prg.programming)
print(prg.coding)
print(prg.eat)
print(prg.walk)

