from sys import stdin,stdout
ans = []
while True:
    l = [int(i) for i in stdin.readline().split()]
    if l[0] == 0:
        ans.insert(0,l[1])
    elif l[0] == 1:
        ans.append(l[1])
    elif l[0] == 2:
        if l[1] in ans:
            ans.insert(ans.index(l[1])+1,l[2])
        else:
            ans.insert(0,l[2])
    elif l[0] == 3:
        if l[1] in ans:
            ans.remove(l[1])
    elif l[0] == 4:
        while l[1] in ans:
            ans.remove(l[1])
    elif l[0] == 5:
        if ans:
            ans.pop(0)
    else:
        break
s=""
for i in range(len(ans)):
    s+=str(ans[i])+" "
stdout.write(s)