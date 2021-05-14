from sys import stdin, stdout
 
def Reshape(x, y, a):   
    k = 0 
    for i in range(x):
        for j in range(y):
            stdout.write(str(a[k]) + " ")
            k += 1
        stdout.write('\n') 

#input
m, n = [int(i) for i in stdin.readline().split()]
r, c = [int(i) for i in stdin.readline().split()]
a = []
for i in range(m):
    row = [int(j) for j in stdin.readline().split()]
    a.extend(row)

#solve & print
if (m * n) != (r * c): Reshape(m, n, a)
else: Reshape(r, c, a)