#polymorphism(manyforms)
#overloading same method diff no of parameter
#overriding  same method same no of argmnt
class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
pe=Student()
pe.show(3,5)
#pe.show(6)#,not support