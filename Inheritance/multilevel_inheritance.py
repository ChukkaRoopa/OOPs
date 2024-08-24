class GrandParent:
    def gdisplay(self):
        print("Grand Parent Class")

class Parent(GrandParent):
    def pdisplay(self):
        print("Parent Class")

class Child(Parent):
    def cdisplay(self):
        print("Child Class")

c = Child()
c.gdisplay()
c.pdisplay()
c.cdisplay()
