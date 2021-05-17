s = list([str(i) for i in input().split()])
noun = 0

def Check(pos):
    for i in s[:pos]:
        if ("lios" not in i) and ("liala" not in i):
            return False
    for i in s[pos+1:]:
        if ("initis" not in i) and ("inites" not in i):
            return False
    return True

for i in s:
    if ("etr" in i) or ("etra" in  i):
        break
    noun += 1

if (Check(noun) == True):
    print("YES")
else:
    print("NO")