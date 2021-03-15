from sys import stdin
from sys import stdout

n, m = list([int(i) for i in stdin.readline().split()])
r, p = list([int(i) for i in input().split()])

if (r*p != n*m):
    for i in range(n):
        arr = stdin.readline()
        stdout.write(arr)
else:
    tmp = 0
    arr = []
    for i in range(n):
        inp = [i for i in input().split()]
        arr += inp

        while (len(arr) >= p):
            stdout.write(" ".join(arr[:p]))
            stdout.write("\n")
            arr = arr[p:]
