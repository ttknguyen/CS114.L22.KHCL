a = str(input())
b = str(input())

def Check(a, b):
    for i in range(0, len(a)):
        if a[i] != b[len(b) - i - 1]:
            return "NO"
    return "YES"

if len(a) != len(b):
    print("NO")
else:
    print(Check(a, b))