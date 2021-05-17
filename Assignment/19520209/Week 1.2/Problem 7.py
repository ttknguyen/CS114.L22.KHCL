import math
n, m, a = list([int(i) for i in input().split()])
x = math.ceil(n/a) * math.ceil(m/a)
print(x)