def solve(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i,j=0,0
    arr=[]
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    arr+=arr1[i:]+arr2[j:]
    return arr
n,m=map(int,input().split())
a = list(map(int,input().strip().split()))[:n]
b = list(map(int,input().strip().split()))[:m]
print(*solve(a,b))