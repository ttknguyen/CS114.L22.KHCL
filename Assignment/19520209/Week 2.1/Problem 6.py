online = set()
while True:
    x = [int(i) for i in input().split()]
    if x[0] == 0:
        break
    elif x[0] == 1:
        online.add(x[1])
    else:
        if x[1] in online:
            print(1)
        else:
            print(0)