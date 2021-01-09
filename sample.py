"'welcome to python world'"

def sample():
    print('welcome to module')
    
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

def mul(*a):
    s = 0
    for i in a:
        s*=i
    return s

def div(*a):
    s = 0
    for i in a:
        s/=i
    return s

def floordiv(*a):
    s = 0
    for i in a:
        s//=i
    return s