online = set()
while True:
    l = [int(i) for i in input().split()]
    if l[0] == 0:
        break
    elif l[0] == 1: online.add(l[1])
    elif l[0] == 3: 
        if (l[1] in online):
            online.clear(l[1])
    elif l[0] == 2:
        if (l[1] in online):
            print(1)
        else:
            print(0)