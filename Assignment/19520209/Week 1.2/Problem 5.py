n = int(input())
list_ = []

for i in range(0, n):
    arr = []
    a, b = list([int(i) for i in input().split()])
    arr.append(a)
    arr.append(b)
    list_.append(arr)

def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);

def RutGon(list_):
    for i in list_:
        x = uscln(i[0], i[1])
        i[0] = i[0] // x
        i[1] = i[1] // x
        if i[1] == 1:
            print(i[0])
        else:
            print(i[0], i[1])
RutGon(list_)