#list1=[1,2,3,4,5,6,7]
#list2=[]
#for i in list1:
 #   list2.append(i*i)
# #print(list2)
# list=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# dup=[]
# for i in list:
#     if i not in dup:
#         dup.append(i)
#     else:
#         print(i)
list=[1,2,3,4,5,8,9]
print(list[::2])
print(list[1::2])
sum=0
n=0
print(list[::2])
for i in list:
    sum=sum+i
    res=sum-list[1]
print(res)

print(sum)

