from sys import stdin, stdout

def GetMaxLen(arr, m, n):
    maxNum = [0]*m
    for j in range(m):
        for i in range(n):
            maxNum[j] = max(maxNum[j], len(str(arr[i][j])))
    return maxNum


#Driver code
n, m = list([int(i) for i in stdin.readline().split()])
arr = []
for i in range(n):
    tmp = [int(i) for i in stdin.readline().split()]
    arr.append(tmp)

maxNum = GetMaxLen(arr, m, n)

for i in range(n):
    for j in range(m):
        a = str(arr[i][j])
        if (len(a) == maxNum[j]):
            stdout.write(a + " ")
        else:
            space = " "*(maxNum[j] - len(a))
            stdout.write(space + a + " ")
    print()