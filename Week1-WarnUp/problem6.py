from decimal import *
getcontext().prec = 6


f = float(input())
c = (f - 32) / 1.8
k = c + 273.15

if (c - int(c) == 0):   c = int(c)
else:   c = Decimal( c ).normalize()

if (k - int(k) == 0):   c = int(k)
else:   k = Decimal( k ).normalize()

print(c, k)