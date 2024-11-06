class Employee:


    @property
    def age(self):
        return 2 * self._age

    @age.setter
    def age(self,age):
        if age <18:
            raise ValueError("Its not correct age ")
        self._age = age+15


obj = Employee()
obj.age = 18
print(obj.age)