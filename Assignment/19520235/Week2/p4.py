from sys import stdin, stdout

h, w = [int(i) for i in stdin.readline().split()]
image = [[int(i) for i in stdin.readline().split()] for j in range(h)]
t, l, b, r = [int(i) for i in stdin.readline().split()]

for i in range(h):
    s = [0]*w
    if (i >= t) and (i <= b):
        s[l:r+1] =  image[i][l:r+1]
    print(*s)