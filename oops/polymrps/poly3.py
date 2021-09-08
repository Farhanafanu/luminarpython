#overriding
#same method,same no of argment,child override parent
#ch.printval("abc")

# class Employee:
#     def value(self,id,salary):
#         self.salary=salary
#         self.id=id
#         print("inside employe method",self.id,self.salary)
#     def value(self,sub,id):
#         self.id=id
#         self.sub=sub
#         print("inside teacher method",self.sub,self.id)
# s=Employee()
# s.value("maths",4)
# s.value(4500,4)
class Book:
    def value(self,name,id):
        self.name=name
        self.id=id
        print(self.name,self.id)
    def value(self,pages,id):
        self.pages=pages
        self.id=id
        print(self.pages,self.id)
b=Book()
b.value(9,9)
