from decimal import *
getcontext().prec = 6
x = float(input())
print(Decimal( x * (0.453592/ (2.54*2.54)) ).normalize())
