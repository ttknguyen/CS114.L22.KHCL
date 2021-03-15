from sys import stdin

s = set()
while True:
    x = [i for i in stdin.readline().split()]
    a=x[0]
    if a == '0':
        break
    elif a == '1':
        b=x[1]
        s.add(b)
    elif a == '2':
        print(int(x[1] in s))
    else:
        if x[1] in s and len(x)==2: 
            s.remove(x[1])
        else:
            continue