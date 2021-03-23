from sys import stdin, stdout
import bisect


# Driver code
n = int(input())
arr = [int(i) for i in stdin.readline().split()]

while True:
    try:
        k,  x = list([int(i) for i in stdin.readline().split()])
        if (x > arr[-1]):
            print(arr[-k], arr[-1])
        elif (x < arr[0]):
            print(arr[0], arr[k-1])
        else:
            pos = bisect.bisect_left(arr, x, 0, len(arr))
            i, j = pos, pos + 1

            for t in range(k):
                if (i < 0):
                    i, j = -1, k
                    break
                if (j == len(arr)):
                    i, j = -k-1, 0
                    break
                if (x - arr[i] <= arr[j]-x):
                    i -= 1
                else:
                    j += 1
                    
            print(arr[i+1], arr[j-1])
    except:
        break
    