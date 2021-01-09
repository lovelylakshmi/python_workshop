def add(*a):
    s = 0
    for i in a:
        s+=i
    return s

def sub(*a):
    s = 0
    for i in a:
        s-=i
    return s

def mul(a,b):
    s = 0
    for i in a:
        s*=i
    return s