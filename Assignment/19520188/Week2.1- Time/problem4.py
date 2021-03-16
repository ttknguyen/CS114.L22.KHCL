from sys import stdin, stdout

n, m = list([int(i) for i in stdin.readline().split()])

arr = []
for i in range(n):
    arr.append([i for i in stdin.readline().split()])

top, left, bottom, right = list([int(i) for i in stdin.readline().split()])

for i in range(n):
    tmp = ['0']*m
    if (i >= top) and i < bottom:
        tmp[left:right+1] = arr[i][left:right+1]
    
    stdout.write(" ".join(tmp) + "\n")