n=int(input())
def solve(n):
    if n<=2:
        return False
    if n%2==0:
        return True
    return False
s=solve(n)
if s==True:
    print("YES")
else:
    print("NO")s