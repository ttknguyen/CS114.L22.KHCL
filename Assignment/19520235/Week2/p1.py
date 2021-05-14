import bisect

def NearestNum(a, k, x):
    mid = bisect.bisect_left(a, x) # return the leftmost index where x can be inserted
    # if x < a[0] => bisect_left() return mid = 0
    # if x > a[n - 1] => bisect_left() return mid = n
    left, right = mid - 1, mid
    k_nearest = []
    # spread to the left and the right of array
    while k > 0:
        if (left < 0) or (right >= len(a)): break
        if abs(x - a[left]) <= abs(x - a[right]):
            k_nearest.append(a[left])
            left -= 1
        else:
            k_nearest.append(a[right])
            right += 1
        k -= 1
    # incase not enough k elements after spreading 
    if k > 0:
        while (left >= 0) and (k > 0):
            k_nearest.append(a[left])
            left -= 1
            k -= 1
        while (right < len(a)) and (k > 0):
            k_nearest.append(a[right])
            right += 1
            k -= 1
    print(*sorted(k_nearest), end = " ")

# input
try:
    n = int(input())
    a = [int(i) for i in input().split()]
    k, x = [int(i) for i in input().split()]
except:
    exit()
    
# main
NearestNum(a, k, x)