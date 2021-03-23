from sys import stdin

test = int(stdin.readline())
while (test > 0):
    n, k = list([int(i) for i in stdin.readline().split()])
    arr = [int(i) for i in stdin.readline().split()]
    print(arr.count(k))
    test -= 1