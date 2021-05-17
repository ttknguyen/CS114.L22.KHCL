n, m = list([int(i) for i in input().split()])
r, c = list([int(i) for i in input().split()])

if n*m != r*c:
    for i in range(n):
        print(input())
else:
    arr = []
    for i in range(n):
        arr += input().split()
        if c < len(arr):
            print(*arr[:c])
            arr = arr[c:]
            r -= 1
    for i in range(0, r):
        print(*arr[i * c:i * c + c])