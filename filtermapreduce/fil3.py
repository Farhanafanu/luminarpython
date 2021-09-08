from functools import reduce
lst=[2,3,4,5,6]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)

def chk_even(num):
    return num%2==0
evens=list(filter(chk_even,lst))
evens=list(filter(lambda num:num%2==0,lst))
oddnum=list(filter(lambda num:num%2!=0,lst))
print(oddnum)
print(evens)
lst=list()
lst.append(10)
print(lst)
from functools import reduce
lst=[2,3,4,5]
sums=reduce(lambda num1,num2:num1+num2,lst)
print(sums)
