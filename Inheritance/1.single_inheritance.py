class Parent:
    def display(self):
        print("Parent Class")

class Child(Parent):
    def show(self):
        print("Child Class")
        
c = Child()
c.display()
c.show()
