class Employee:

    def __init__(self):
        self.__name = "Rajan"

ob = Employee()
# print(ob.__name) # cant access directlty

print(ob._Employee__name)

print(ob.__dir__())