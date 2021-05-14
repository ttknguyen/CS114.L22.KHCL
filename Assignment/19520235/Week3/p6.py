from sys import stdin, stdout

q = int(stdin.readline())
for i in range(q):
    n, k = [int(i) for i in stdin.readline().split()]
    a = tuple(int(i) for i in stdin.readline().split())
    stdout.write(str(a.count(k)) + '\n')