class Student:

    def __init__(self,name,major, gpa ,is_probation):
        print("Comes inside costructor")
        self.name= name
        self.major = major
        self.gpa = gpa
        self.is_probation = is_probation

    def on_honour(self):
        if self.gpa >=3.4:
            return True
        else:
            return False