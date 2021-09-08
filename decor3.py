def age_required(func):
    def wrapper(n,a,p):
        if a<18:
            raise Exception("not eligible")
        else:
            return func(n,n,p)
    return wrapper
@age_required
def vaccine(name,age,place):
    return "eligible"

print(vaccine("arun",22,"malprm"))
print(vaccine("abi",15,"kochi"))
