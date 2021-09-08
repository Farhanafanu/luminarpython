class Vehicle:
    def setval(self,number,id,color):
        self.number=number
        self.id=id
        self.color=color
        print(self.number,self.id,self.color)
class Bus(Vehicle):
    def setv(self,refno):
        self.refno=refno
        print(self.refno)
b=Bus()
b.setv(2)
b.setval(1,23,"red")

