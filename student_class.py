class student:
    rno = 63
    name = "roopa"
    branch = "cse"
    def read(self):
        rno = 15
        print("rollno=", rno)
        print("Instance variable=",self.rno)
        print("Reading..")
    def write(self):
        print("Writing..")

abc = student()
obj = student()
print("rno=", abc.rno)
print("name=",abc.name)
print("branch=", abc.branch)
abc.read()
abc.write()
obj.read()