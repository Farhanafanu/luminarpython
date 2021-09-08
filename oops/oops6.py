class Person:#constructor
   def __init__(self,name,age,address):#init=construcor used to initialize instance variable
       self.name=name
       self.age=age
       self.address=address
   def printval(self):
      print(self.name,self.age,self.address)
obj=Person("anu",19,"okhrfgtt")
obj.printval()
class Teacher:
    college="ma college"
    def __init__(self,name,id,subject,department):
        self.name=name
        self.id=id
        self.subject=subject
        self.department=department
    def printval(self):
        print(self.name,self.id,self.subject,self.department)
        print(Teacher.college)
t=Teacher("shiji",9,"maths","cse")
te=Teacher("suju",5,"complier","cse")
t.printval()
te.printval()

    