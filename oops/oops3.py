class Employee:
    def setvalue(self,name,id,salary,companyname):
        self.name=name
        self.id=id
        self.salary=salary
        self.companyname=companyname
    def printvalue(self):
        print(self.name,self.id,self.salary,self.companyname)
emp=Employee()
emp.setvalue("anu",2,45000,"luminar")
emp.printvalue()
class Employee:
    comanyname="tcs"
    def setval(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printval(self):
        print(self.id,self.name,self.salary)
        print(Employee.comanyname)

e=Employee()
e.setval(2,"aslu",60000)
e.printval()