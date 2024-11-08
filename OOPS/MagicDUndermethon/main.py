class Employee:

    name = "Mohit"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    # def __str__(self):
    #     return f"The Name of the employee is {self.name}"

    def __repr__(self):
        return f"The Name of the employee is {self.name} repr reeee"

    def __call__(self):
        print("I am calling....")


e = Employee()
print(e)
# print(e.name)
# print(len(e))
e()