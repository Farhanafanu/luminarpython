class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def setv(self,clas,age):
        self.clas=clas
        self.age=age
        print(self.clas,self.age)
class Parent(Person):
    def setp(self,name,adrs):
        self.name=name
        self.adrs=adrs
        print(self.name,self.adrs)
class Student(Child):
    def sets(self,name,std):
        self.name=name
        self.std=std
        print(self.name,self.std)
st=Student()
st.sets("bn",7)
st.set("lossd",8)
st.setv(4,9)