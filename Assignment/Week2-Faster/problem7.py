from math import *

n, m, a = list([int(i) for i in input().split()])
ans = ceil(n / a) * ceil(m / a)
print(ans)