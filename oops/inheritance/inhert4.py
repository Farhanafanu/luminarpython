class Person:
    def detals(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def setval(self,name,age,qlfn):
        self.name=name
        self.age=age
        self.qlfn=qlfn
        print(self.name,self.age,self.qlfn)
class Student(Child):
    def vals(self,salary,id):
        self.salary=salary
        self.id=id
        print(self.salary,self.id)
s=Student()
s.setval("abitha",40,"btech")
s.detals("ajmi",25)
s.vals(45000,5)
#person,parent,teacher