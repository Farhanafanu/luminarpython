#inheritance
# class Person:
#     def walk(self):
#        print("person is walking")
#     def read(self):
#         print("person reading")
# class Student(Person):
#     def exam(self):
#         print("student attending exam")
# pe=Person()
# pe.walk()
# pe.read()
# st=Student()
# st.exam()
# st.read()
#st.walk()#single inherittance,parent class,or baseclass,super class(person)
#child class,derived class,subclass(student)
class Person:
    def walk(self):
        print("person is waking")
    def Study(self):
        print("person is studing")
    def sleep(self):
        print("person is sleeping")
class Student(Person):
    def Exam(self):
        print("person attending exam")

s=Student()
s.Exam()
s.walk()
s.sleep()
s.Study()