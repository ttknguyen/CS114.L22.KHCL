import math
a = float(input())
b = float(input())
c = float(input())

def Check(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        return False
    return True

def DienTich(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if (s - round(s, 0) == 0):
        return int(s)
    return round(s, 2)

def TamGiac(a, b, c):
    d = DienTich(a, b, c)
    if a == b == c:
        return "Tam giac deu"
    if a == b or a == c or b == c:
        return "Tam giac can"
    if (a * a + b * b) == c * c or (a * a + c * c) == b * b or (c * c + b * b) == a * a:
        return "Tam giac vuong"
    else:
        return "Tam giac thuong"

if (Check(a, b, c) == True):
    print(TamGiac(a, b, c) + ", dien tich =", DienTich(a, b, c))
else:
    print('Khong phai tam giac')