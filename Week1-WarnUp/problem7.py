a, b = list([int(i) for i in input().split()])

y = (b - 2*a) / 2
x = a - y
print(int(x), int(y))
