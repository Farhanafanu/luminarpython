class Person:
    def dtls(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def pars(self,parentname,parentaddrs):
        self.parentname=parentname
        self.parentaddrs=parentaddrs
        print(self.parentname,self.parentaddrs)
class Teacher(Parent,Person):
    def valu(self,salary,subject):
        self.salary=salary
        self.subject=subject
        print(self.salary,self.subject)
t=Teacher()
t.dtls("aslu",25)
t.pars("muhamed","nc")
t.valu(60000,"maths")