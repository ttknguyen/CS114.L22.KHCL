n = int(input())
arr = []

while (n > 0):
    arr.append(n % 10)
    n = n // 10

'''dem so chu so may man'''
count = arr.count(4) + arr.count(7)
count_ = count
arr_ = []

while (count_ > 0):
    arr_.append(count_ % 10)
    count_ = count_ // 10


def SoMayMan(n):
    for i in arr_:
        if i != 4 and i != 7:
            return False
    return True


if count < 4:
    print("NO")
else:
    if SoMayMan(count) == True:
        print("YES")
    else:
        print("NO")