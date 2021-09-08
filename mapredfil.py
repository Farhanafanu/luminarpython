lst=[2,3,4,5,6]
#map (function,list/iterable)
def square(num):
    return  num**2
squrs=list(map(square,lst))
print(squrs)
square=list(map(lambda num:num**2,lst))
print(square)


def cube(num):
    return num**3
cubes=list(map(cube,lst))
print(cubes)
cubee=list(map(lambda num:num**3,lst))
print(cubee)