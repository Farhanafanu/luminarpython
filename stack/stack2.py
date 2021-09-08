stk=[]
size=int(input("enter size"))
top=0
n=0
def push():
    global size,top
    if top>size:
        print("stack is full")
    else:
        p=int(input("enter elemnt to push"))
        stk.append(p)
        top+=1
def pop():
    global size,top
    if top<=0:
        print("stack is empty")
    else:
        stk.pop()
        top-=1
def display():
    print(stk)
while(n!=1):
    print("enter option")
    opt=int(input("press1.push,2.pop,3.display"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    else:
        display()