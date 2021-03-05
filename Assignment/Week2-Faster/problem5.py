def GDC(a, b):
    if(b==0): 
        return a 
    else: 
        return GDC(b,a%b)
#Driver code
q = int(input())
for i in range(q):
    a, b = list([int(i) for i in input().split()])
    g = GDC(a, b)
    if (b // g != 1):
        print(a // g, b // g)
    else:
        print(a//g)