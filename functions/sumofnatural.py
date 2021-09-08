#num=int(input("enter the number"))
#def sum(n):
   # if n<=1:
        # return (n)
   # else:
     # return  n+sum(n-1)
#print("sum is",sum(num))
def sum(n):
    s=0
    for i in range(n+1):
        s=s+i
    print(s)#return s
sum(10)#print(sum(5))




