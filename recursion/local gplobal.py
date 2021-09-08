x=5
a=7
def foo():
    #x=3
    global x,a
    x+=10
    a+=5
    #print("local x",x,a)
foo()
print("global x",x,a)