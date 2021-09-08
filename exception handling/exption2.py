list=[1,2,3,4]
index=int(input("enter size"))
try:
    print(list[index])
except Exception as h:
    print(h.args)
finally:
    print("inside")
num=int(input("enter num"))
num2=int(input("enter num"))
try:
    res=num/num2
    print(res)
except Exception as a:
    print(a.args)
finally:
    print("inside")