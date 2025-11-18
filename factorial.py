def fact(fact):
    res=1
    for i in range(2,fact+1):
        res=res*i
    return res
print(fact(10))