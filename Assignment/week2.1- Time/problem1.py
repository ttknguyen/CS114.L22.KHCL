def BinSearch(arr, x):
  i, j = 0, len(arr) -1 
  while (i <= j):
    mid = (i + j) // 2
    if (arr[mid] == x):
      break
    elif (arr[mid] < x):
      i = mid + 1
    elif (arr[mid] > x):
      j = mid - 1
  return mid

def KNearest(arr, k, x):
    pos = BinSearch(arr, x)
    i, j = pos, pos + 1

    ans = []
    while (k > 0):
        if (i < 0) or (j >= len(arr)):
            break
        if (abs(arr[i] - x) <= abs(arr[j] - x)):
            ans.append(arr[i])
            i -= 1
        else:
            ans.append(arr[j])
            j += 1
        k -= 1


    if (k > 0):
        while (i >= 0) and (k > 0):
            ans.append(arr[i])
            i -= 1
            k -= 1
            
        while (j < len(arr)) and (k > 0):
            ans.append(arr[j])
            j += 1
            k -= 1

    return sorted(ans)
    
#Driver code
n = int(input())
arr = [int(i) for i in input().split()]
k, x = list([int(i) for i in input().split()])
print(*KNearest(arr, k, x), end = ' ')