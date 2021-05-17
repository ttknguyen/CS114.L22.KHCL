n = int(input())
arr = [int(i) for i in input().split()]
k, x = list([int(i) for i in input().split()])
tmp = 0
for i in arr[k:]:
    if abs(x-i) <= abs(x-arr[tmp]):
        tmp += 1
    else:
        break
print(*arr[tmp:tmp+k])