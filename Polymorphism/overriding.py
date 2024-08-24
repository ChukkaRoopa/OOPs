class Father:
    def transport(self):
        print("cycle")

class Son(Father):
    def transport(self):
        print("Bike")

obj = Son()
obj.transport()