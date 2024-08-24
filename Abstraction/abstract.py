from abc import ABC,abstractmethod

class AbstractDemo(ABC): # Abstact class
    @abstractmethod       # Abstract method
    def display(self):  
        None
    @abstractmethod       # Abstact method
    def show(self):
        None

class Demo(AbstractDemo):   # Abstract class
    def display(self):
        print("Abstract method")

class Demo1(AbstractDemo):   # Concrete class
    def show(self):
        print("Show method")
    def display(self):
        print("display method")

obj = Demo1()
obj.display()
obj.show()
