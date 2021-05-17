q = int(input())

def check(arr, n, k):
    dem = 0
    for i in range(n):
        if arr[i] == k:
            dem += 1
    print(dem)

for i in range(q):
    n, k = list([int(i) for i in input().split()])
    arr = [int(i) for i in input().split()]
    check(arr, n, k)