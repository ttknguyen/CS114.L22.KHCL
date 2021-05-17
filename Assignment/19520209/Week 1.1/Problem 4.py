from decimal import *
getcontext().prec = 6

p = float(input())
k = 0.453592/(2.54*2.54)
r = Decimal(p*k).normalize()

print(r)