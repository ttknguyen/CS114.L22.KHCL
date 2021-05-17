from sys import stdin, stdout
h, w = [int(i) for i in stdin.readline().split()]

row = []
for i in range(h):
    row.append([int(i) for i in stdin.readline().split()])

top, left, bottom, right = [int(i) for i in stdin.readline().split()]

for i in range(h):
    k = [0]*w
    if i >= top and i <= bottom:
        k[left:right+1] = row[i][left:right+1]
    print(*k)