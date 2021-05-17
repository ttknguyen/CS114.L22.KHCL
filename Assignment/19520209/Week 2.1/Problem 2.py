from sys import stdin, stdout
list = []

while True:
    x = [int(i) for i in stdin.readline().split()]
    if x[0] == 0:
        list.insert(0, x[1])
    elif x[0] == 1:
        list.append(x[1])
    elif x[0] == 2:
        if x[1] not in list:
            list.insert(0, x[2])
        else:
            list.insert(list.index(x[1])+1, x[2])
    elif x[0] == 3:
        if x[1] in list:
            list.remove(x[1])
    elif x[0] == 4:
        while x[1] in list:
            list.remove(x[1])
    elif x[0] == 5:
        if list:
            list.pop(0)
    else:
        break
s = ""
for i in range(len(list)):
    s += str(list[i])+" "
stdout.write(s)