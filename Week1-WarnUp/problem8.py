def posB(n, k, p, q):
    if (k == n): return [-1]

    tmp = 2 * (p-1) + q
    codeA =  tmp % k 
    if (codeA == 0): codeA = k

    pos1 = tmp - k
    if (pos1 > 0): 
        if (pos1 % 2 == 0):
            pos1 = [ ( (pos1-2) // 2) + 1, 2]
        else:
            pos1 = [ ( (pos1-1) // 2) + 1, 1]
    else: pos1 = [1e9, 2]

    pos2 = tmp + k
    if (pos2 <=  n): 
        if (pos2 % 2 == 0):
            pos2 = [ ( (pos2-2) // 2) + 1, 2]
        else:
            pos2 = [ ( (pos2-1) // 2) + 1, 1]
    else: pos2 = [1e9, 2]

    if (pos2[0] - p < pos1[0] ):
        return pos2
    if (p - pos1[0] <= pos2[0] ):
        return pos1
    return [-1]


# Drive code
n = int(input())
k = int(input())
p = int(input())
q = int(input())
print(*posB(n, k, p, q), end = ' ')