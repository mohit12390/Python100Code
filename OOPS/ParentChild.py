class Parent:

    def parent_method(self):
        print("Parent method()")

class Child(Parent):

    def child_method(self):
        print("Chiled method()")
        super().parent_method()


childobject = Child()
childobject.child_method()