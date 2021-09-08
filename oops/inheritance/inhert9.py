# class Vehicle:
#     def  __init__(self,model,regno,color):
#          self.model=model
#          self.regno=regno
#          self.color=color
#     def printval(self):
#          print(self.model,self.regno,self.color)
#     def __str__(self):
#          return self.model+self.color
# v=Vehicle("rg",34567,"red")
# v.printval()
# print(v)
#two string method,not use comma
class Student:
    college="NIT"
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
    def prints(self):
        print(self.name,self.rollno,self.dept,Student.college)
    def __str__(self):
        return self.dept+self.name
s=Student("fanu",10,"cse")
s.prints()
print(s)