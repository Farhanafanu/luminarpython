# class Person:
#     def setvalue(self,name,age):
#         self.name=name
#         self.age=age
#     #def printvalue(self):
#         print("name",self.name)
#         print("age",self.age)
# pe=Person()
# pe.setvalue("anu",26)
# #pe.printvalue()
class Animal:
    def __init__(self,name,specis,adaption):
        self.name=name
        self.specis=specis
        self.adaption=adaption
        print(self.name,self.specis,self.adaption)
class Frog(Animal):
    def __init__(self,name):
        self.name=name=name
        print(self.name)
f=Frog("abd")
f=Frog("aji,nau,sju")