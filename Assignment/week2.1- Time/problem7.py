from sys import stdin

sta = set()
while True:
    x = [int(i) for i in stdin.readline().split()]
    a=x[0]
    if a == 0:
        break
    elif a == 1:
        b=x[1]
        sta.add(b)
    elif a == 2:
        print(int(x[1] in sta))
    else:
        if x[1] in sta and len(x)==2: 
            sta.remove(x[1])
        else:
            continue