class Father:
    def fdisplay(self):
        print("Father classs")

class Mother:
    def mdisplay(self):
        print("Mother class")

class child(Father, Mother):
    def cdisplay(self):
        print("Child class")

c1 = child()
c1.fdisplay()
c1.mdisplay()
c1.cdisplay()