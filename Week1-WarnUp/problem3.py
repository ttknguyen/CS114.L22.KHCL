import math

def checkTri(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    return True

def Classify(a, b, c):
    if (a == b) and (a == c):
        return "Tam giac deu,"
    
    if (a == b) or (b == c) or (a == c):
        return "Tam giac can,"
    
    if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        return "Tam giac vuong,"
    
    return "Tam giac thuong,"

def Heron(a, b, c):
    p = float(a + b + c) / 2
    s = math.sqrt( p* (p - a)* (p - b)* (p - c) )
    
    if (s - round(s, 0) == 0):
        return int(s)
    return round(s, 2)

# Input
a = int(input())
b = int(input())
c = int(input())

if (checkTri(a, b, c)):
    print(Classify(a, b, c), "dien tich = ", Heron(a, b, c))
else:
    print("Khong phai tam giac")