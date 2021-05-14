from sys import stdin, stdout

# input & initialize
r, c = [int(i) for i in stdin.readline().split()]
a2D = []
max_length = [0] * c
for i in range(r):
    a = [int(x) for x in stdin.readline().split()]
    for j in range(c):
        max_length[j] = max(max_length[j], len(str(a[j])))
    a2D.append(a)

# solve & print
for i in range(r):
    for j in range(c):
        # align margin-right by filling " " on the left of each element (if len < max)
        stdout.write(str(a2D[i][j]).rjust(max_length[j], " "))
        if j < c - 1:
            stdout.write(" ") # if not the last element, print " "
        else:
            stdout.write("\n") # print "\n" on the right of the last element