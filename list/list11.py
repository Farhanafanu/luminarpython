numbers=[1,2,3,4,5,6,7,8,9,10]
even=[i for i in numbers if i%2==0 ]
print(even)
odd=[i for i in numbers if i%2!=0]
print(odd)
#100-200 even numbers 2lines
even=[i for i in range(100,200) if i%2==0]
print(even)
numbers=[1,2,3,4,5,6,7,8,9,10]
res=1
for i in numbers:
   res=res*i
print(res)
a=[1,2,3,4,5]
a[0]=10
print(a)
a=[1,9,8]
b=["arun","hey"]
a.extend(b)
print(a)

