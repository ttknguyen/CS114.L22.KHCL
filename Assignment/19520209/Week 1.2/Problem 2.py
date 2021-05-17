from math import *
q = int(input())

for i in range(q):
    sp = int(input())
    gia = [int(i) for i in input().split()]
    print(ceil(sum(gia)/sp))