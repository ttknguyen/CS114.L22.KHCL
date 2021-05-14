from sys import stdin

li = []
while True:
    form = [int(i) for i in stdin.readline().split()]
    if form[0] == 0: 
        li.insert(0, form[1])
    elif form[0] == 1: 
        li.append(form[1])
    elif form[0] == 2: 
        if form[1] in li: 
            li.insert(li.index(form[1]) + 1, form[2])
        else:
            li.insert(0, form[2])
    elif form[0] == 3: 
        if form[1] in li:
            li.remove(form[1])
    elif form[0] == 4: 
        while form[1] in li:
            li.remove(form[1])
    elif form[0] == 5:
        if len(li) > 0: li.pop(0)
    else:
        break
print(*li, end = " ")