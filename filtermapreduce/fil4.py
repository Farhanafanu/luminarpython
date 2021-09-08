lst=[2,4,6]
#list1=[3,5,7]
op=[]
sum=0
for i in lst:
    op.append(sum-i)
print(op)
    # sum=0
# list=[]
# for i in list1:
#     list.append([i-1]+[i+1])
#     sum=sum+list
# print(list)
# print(sum)
    #sum=sum+i
#print(sum)
#print(sum-lst[0],sum-lst[1],sum-lst[2])
# list1=[2,3,4,5]
# total=6
# for i in list1:#2,3
#     for j in list1:#2,3start
#         if (i!=j):#2,2,
#             if (total==(i+j)):#2+3,2+4
#                 print(i,j)
# lst=[2,3,4,5]
# for i in range(0,len(lst)):
#     for j in range(1,len(lst)):
#         if(lst[i]+lst[j]==6):
#
#
#             print(lst[i],lst[j])
lst=[1,2,3,4,5]
low=0
upp=len(lst)-1
pair=6
pairs=[]
count=0
while(low<upp):
    sum=lst[low]+lst[upp]
    if (sum==pair):
        print(lst[low],lst[upp])
        pairs.append((lst[low],lst[upp]))
        low+=1
        #break
    elif(sum>pair):
        upp-=1
    elif (sum<pair):
        low+=1
        count+=1
print(count)
#print(pairs)




