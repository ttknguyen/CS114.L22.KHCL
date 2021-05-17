n, m = list([int(i) for i in input().split()])
l = len(str(n))
if (m % (10**l) >= n):
    print(m//(10**l) + 1)
else:
    print(m//(10**l))