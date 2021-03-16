from sys import stdin
from sys import stdout

s = set()
while True:
    x = [int(i) for i in stdin.readline().split()]
    if (len(x) == 0):
        continue
    if x[0] == 0:
        break
    elif x[0] == 1:
        s.add(x[1])
    elif x[0] == 2:
        tmp = int(x[1] in s)
        stdout.write(str(tmp) + '\n')
    else:
        if x[1] in s: 
            s.discard(x[1])
        else:
            continue