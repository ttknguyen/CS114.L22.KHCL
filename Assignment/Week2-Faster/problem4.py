def check(s, posT):
    for i in range(posT):
        tmp = s[i]
        if ("lios" != tmp[-4:]) and ("liala" != tmp[-5:]):
            return False
    for i in range(posT+1, len(s)):
        tmp = s[i]
        if ("initis" != tmp[-6:]) and ("inites" != tmp[-6:]):
            return False
    return True

s = [i for i in input().split()]

posN = 0
for i in s:
    if ("etr" in i) or ("etra" in i):
        break
    posN += 1

if (check(s, posN)):
    print("YES")
else:
    print("NO")