from math import *
#Driver code
q = int(input())
for i in range(q):
    n = int(input())
    s = sum([int(i) for i in input().split()])
    print(ceil(s/n))