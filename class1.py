#Simple code for class 
class Box:
    def __init__(self,nameofStudent,rollno):
        self.name = nameofStudent
        self.rollno = rollno

obj1 = Box("govind",76)
obj2=Box("raj",54)
print(obj1.name)
print(obj2.name)

Output
govind
raj
