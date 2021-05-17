from decimal import *
getcontext().prec = 6

F = float(input())
C = (F - 32) / 1.8
K = C + 273.15

if (C - round(C, 0) == 0):
    C = int(C)
else:
    C = Decimal(C).normalize()

if (K - round(K, 0) == 0):
    K = int(K)
else:
    K = Decimal(K).normalize()

print(C, K)