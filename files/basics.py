#f=open('abg','w')
#.write("hello")
#f.write("hai")
#f.write("hello")
# f1=open('abg','r')
# f2=open('abc','w')
# for i in f1:
#     f2.write(i)
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print(self.name,self.age)
#     def __str__(self):
#         return self.name
# f1=open("student","r")
# for line in f1:
#     print(line)
#     l=line.split(",")
#     print(l)
#     name=l[0]
#     age=l[1]
#     st=Student(name,age)
#     print(st)
#     st.printval()
class Student:
    def __init__(self,name,age,course,mark):
        self.name=name
        self.age=age
        self.course=course
        self.mark=mark
    def printval(self):
        print(self.name,self.age,self.course,self.mark)
    def __str__(self):
        return self.name
f1=open("student","r")
for line in f1:
    print(line)
    l=line.split(",")
    name=l[0]
    age=l[1]
    course=l[2]
    mark=l[3]
    st=Student(name, age, course, mark)
    print(st)
    st.printval()