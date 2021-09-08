class Calcu:
    def __init__(self):
        self.num1=num1
        self.num2=num2
    def add(self):
         return self.num1+self.num2
    def sub(self):
         return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
num1=int(input("enter"))
num2=int(input("enter"))
c=Calcu()
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())