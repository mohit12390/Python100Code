class Animal:

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def make_sound(self):
        print("Animal is making sound ")

class Cat(Animal):

    def __init__(self,name,sound):
        super().__init__(name,type)
        self.sound = sound

    def make_sound(self):
        print("Meoww meoww !!")


ca = Cat("ranchi","Meow")
ca.make_sound()
print(ca.sound,ca.name)

