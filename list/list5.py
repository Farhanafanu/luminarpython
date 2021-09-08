# list1=[0,1,2,2,3,3,34,5,6,78,90,80,99,88]
# def linearsearch(list1):
#     ele=int(input("enter element to search"))
#     flag=0
#     for i in list1:
#         if i==ele:
#             flag=1
#             break
#     if flag==0:
#         print("not found")
#     else:
#         print("found")
list=[1,2,3,4,5,6,7,8,9,10]
def linearsearch(list):
    ele=int(input("enter element to search"))
    flag=0
    for i in list:
        if i ==ele:
            flag=1
            break
    if flag==0:
        print("not found")
    else:
        print("found")
linearsearch(list)
