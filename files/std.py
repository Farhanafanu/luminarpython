class Student:
    def __init__(self,name,numb,course,mark):
        self.name=name
        self.numb=numb
        self.course=course
        self.mark=mark
    def printval(self):
        print(self.name,self.numb,self.course,self.mark)
    def __str__(self):
        return self.name
f1=open("student",'r')
for line in f1:
    print(line)
    l=line.split(",")
    print(l)
    name=l[0]
    numb=l[1]
    course=l[2]
    mark=l[3]
    st=Student(name,numb,course,mark)
    st.printval()
    print(st)