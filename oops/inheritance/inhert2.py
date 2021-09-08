class Person:
    def detals(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.course)
class Employe(Person):
    def company(self,department,salary,id):
        self.department=department
        self.salary=salary
        self.id=id
    def printsv(self):
        print(self.department)
        print(self.salary)
        print(self.id)

# p=Person()
# p.detals("anu",8,"bed")
# p.printval()
e=Employe()
e.company("luminar",45000,34)
#e.printsv()
e.detals("ajaman",12,"btech")
#e.printval()



