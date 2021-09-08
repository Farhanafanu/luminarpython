class Add:
     def set(self,num1,num2):
         self.num1=num1
         self.num2=num2
         print(self.num1+self.num2)
add1=Add()
num1=int(input("enter"))
num2=int(input("enter"))
add1.set(num1,num2)
class student:
    name='luminar'#static variable(related to class,call using class name),instance variable(rd ,call by self)
    def set(self,rollno,classname):
        self.rollno=rollno
        self.classname=classname
    def printval(self):
        print(self.rollno)
        print(self.classname)
        print(student.name)
a=student()
a.set(2,4)
a.printval()