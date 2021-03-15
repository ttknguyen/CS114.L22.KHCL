def posB(n, k, p, q):
    posA = 2 * (p-1) + q
    pos1 = posA - k
    pos2 = posA + k
    if(pos1 > 0):
        print((pos1+1)//2, q if k % 2 == 0 else q % 2 + 1) 
        return

    if(pos2 <= n):
        print((pos2+1) // 2, q if k % 2 == 0 else q % 2 + 1)
        return

    print(-1)
    return

# Drive code
n = int(input())
k = int(input())
p = int(input())
q = int(input())
posB(n, k, p, q)