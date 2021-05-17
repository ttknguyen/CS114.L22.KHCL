import bisect as bi
n = int(input())
arr = [int(i) for i in input().split()]
while True:
    a = [int(i) for i in input().split()]
    if len(a) == 0:
        break
    k, x = a[0],a[1]
    if x > arr[-1]:
        print(arr[-k],arr[-1])
    elif x < arr[0]:
        print(arr[0],arr[k-1])
    else:
        pos = bi.bisect_left(arr,x,0,len(arr))
        j = pos
        h = pos +1
        for i in range(k):
            if j < 0:
                j = -1
                h = k
                break
            if h == len(arr):
                j = -k-1
                h = 0
                break
            if x - arr[j] <= arr[h] - x:
                j -= 1
            else:
                h += 1
        print(arr[j+1],arr[h-1])