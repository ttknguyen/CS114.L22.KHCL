q = int(input())


def Check():
    a = len(s)
    b = len(t)
    if a != b:
        return False
    for i in range(a):
        if s[i] in t:
            return True
    return False


for i in range(q):
    s = list(input())
    t = list(input())
    if Check():
        print("YES")
    else:
        print("NO")