employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
total=0
for employee in employees:
    print(employee["e_name"])#map
    print(employee["e_name"].upper())

    total+=employee["salary"]
    print(employee["salary"])#reduce
    print(total)
    if (employee["department"]=="developer"):#filter
        print(employee["e_name"])
        e_names=list(map(lambda employee:employee["e_name"],employees))
        e_upper=list(map(lambda employee:employee["e_name"].upper(),employees ))
        deveolpers_name=list(map(lambda develeper:develeper["e_name"],employees))
        salaries=sum(list(map(lambda emp:emp["salary"],employees)))
        salarie=max(list(map(lambda emp:emp["salary"],employees)))
        salryss=min(list(map(lambda emp:emp["salary"],employees)))
print(salryss)
print(salarie)
print(salaries)
print(e_upper)
print(e_names)
print(deveolpers_name)
# print()
