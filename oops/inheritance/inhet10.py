class Parent:
    def __init__(self,age,addrs):
        self.age=age
        self.addrs=addrs
    def printv(self):
        print(self.age,self.addrs)
class Teacher(Parent):
    def __init__(self,name,id,age,addrs):
        super().__init__(age,addrs)
        self.name=name
        self.id=id
    def printd(self):
        print(self.name,self.id,self.age,self.addrs)
    def __str__(self):
        return self.name+str(self.id)
t=Teacher("anu",89,33,"abc")
t.printd()
print(t)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvs(self):
        print(self.name,self.age)
class Employe(Person):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    def printb(self):
        print(self.name,self.age,self.id,self.salary)
    def __str__(self):
        return self.id+self.salary
e=Employe("fanu",23,'8907','45000')
e.printb()
print(e)