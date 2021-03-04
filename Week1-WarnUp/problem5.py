a, b = list([int(i) for i in input().split()])
tmp = b % (2 * a)
if (tmp < a):
    print(tmp)
else:
    print(2*a - tmp)