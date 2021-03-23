n, m = list([int(i) for i in input().split()])

tmp = n
k = 0
while (tmp > 0):
    tmp = tmp // 10
    k += 1

tmp = (m // 10**k) * 10**k
ans = m// 10**k
if (tmp + n <= m):
    print(ans+1)
else:
    print(ans)