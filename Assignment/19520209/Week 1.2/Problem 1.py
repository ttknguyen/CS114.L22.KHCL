import math
n = int(input())
n_ = n
sum = 0

def SoChuSo(n):
    d = 0
    while(n>0):
        d += 1
        n = n // 10
    return d

k = SoChuSo(n)

for i in range (0, k):
    m = n_ % 10
    sum += pow(m, k)
    n_ = n_ // 10

if (sum == n):
    print("True")
else:
    print("False")