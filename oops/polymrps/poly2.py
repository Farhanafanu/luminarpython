class Student:
     def show(self,name):
         self.name=name
         print(self.name)
class Teacher(Student):
    def show(self,sub,id):
        self.sub=sub
        self.id=id
        print(self.sub,self.id)
t=Teacher()
t.show("maths",4)
#t.set("science")
class Operator:
    def num(self,num1,num2):
         self.num1=num1
         self.num2=num2
         print(self.num1,self.num2)
    def num(self,num3):
         self.num3=num3
         print(self.num3)
np=Operator()
#np.num(3,4)
np.num(1)