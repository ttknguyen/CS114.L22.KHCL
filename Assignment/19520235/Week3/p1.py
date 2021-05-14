from sys import stdin
import bisect

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]

def KCloset(a, k, x):
    found = bisect.bisect_left(a, x, 0, len(a) - 1)
    if found + 1 < len(a) and a[found] != x:
        if abs(x - a[found]) > abs(x - a[found + 1]):
            found += 1
    left = max(0, found - k + 1)
    right = left + k - 1
    while (right + 1) < len(a) and abs(a[right + 1] - x) < abs(x - a[left]):
        left += 1
        right += 1
    print(a[left], a[right])

try:
    while True:
        k, x = [int(x) for x in stdin.readline().split()]
        KCloset(a, k, x)
except: 
    exit() 
