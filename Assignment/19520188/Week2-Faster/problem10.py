def check(a, b):
    for i in a:
        if i in b:
            return True
    for i in b:
        if i in a:
            return True
    return False

    
#Driver code
q = int(input())
for i in range(q):

    a = input()
    b = input()

    if (a == b):
        print("YES")
    else:
        if (check(a, b)):
            print("YES")
        else:
            print("NO")