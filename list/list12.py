list=[1,7,5,2,9,3,0,4,6]
def bsearch():
    list.sort()
    print(list)
    ele=int(input("enter element to search"))
    flag=0
    low=0
    upp=len(list)-1
    while low<=upp:
        mid=(low+upp)//2
        if ele>list[mid]:
            low=mid+1
        elif ele<list[mid]:
            upp=mid-1
        elif ele==list[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("notfound")
bsearch()




