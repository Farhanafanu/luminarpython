# mylist=[111,-15,3,43,20,10]
# newlist=[]
# while mylist:
#     min=mylist[0]
#     for i in mylist:
#         if i<min:
#             min=i
#     newlist.append(min)
#     mylist.remove(min)
# print(newlist)
#print(mylist)
mylist=[10,-3,4,-5,8]
newlist=[]
while mylist:
    min=mylist[0]
    for i in mylist:
        if i<min:
            min=i
    newlist.append(min)
    mylist.remove(min)

print(newlist)
print(mylist)