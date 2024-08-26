class Instructor:
    def __init__(self,instructor_name,address):
        self.name = instructor_name
        self.address = address
        self.followers = 0

instructor1 = Instructor("Roopa","Vizag")
print(instructor1.name)
print(instructor1.followers)