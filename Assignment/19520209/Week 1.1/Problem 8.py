n = int(input())
k = int(input())
p = int(input())
q = int(input())

k_ = (p-1) * 2 + q
before = k_ - k
after = k_ + k

if before > 0:
    print((before+1) // 2, q if k % 2 == 0 else q % 2 + 1)
elif after <= n:
    print((after+1) // 2, q if k % 2 == 0 else q % 2 + 1)
else:
    print(-1)