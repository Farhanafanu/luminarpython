# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# try:
#     res=num1/num2
#     print(res)
# except:
#      print("exception occured")
list=[1,2,3,4]
index=int(input("enter the index"))
try:
     print(list[index])
except:
    print("exception occured")
finally:
   print("inside finally")
