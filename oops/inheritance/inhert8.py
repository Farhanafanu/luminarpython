class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
st=Student(2,33,"anu",24)
st.printval()
st.print()

class Employee(Person):
    def __init__(self,id,salary,name,age):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    def printv(self):
        print(self.id)
        print(self.salary)
e=Employee(2,45000,"aslu",25)
e.printv()
e.printval()