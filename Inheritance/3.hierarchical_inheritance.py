class Parent:
    def pdisplay(self):
        print("Parent")

class child1(Parent):
    def c1display(self):
        print("Child 1")

class child2(Parent):
    def c2display(self):
        print("Child 2")

c1 = child1()
c2 = child2()

c1.pdisplay()
c1.c1display()
c2.pdisplay()
c2.c2display()