from sys import stdin, stdout

n, m = [int(i) for i in stdin.readline().split()]
exp = len(str(n))
count = m // pow(10, exp)
if n <= (m % pow(10, exp)): count += 1
print(count)