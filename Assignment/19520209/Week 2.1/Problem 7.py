from sys import stdin, stdout
log_in = set()
while True:
    x = ([int(i) for i in stdin.readline().split()])
    if len(x) == 0:
        continue
    if x[0] == 0:
        break
    elif x[0] == 1:
        log_in.add(x[1])
    elif x[0] == 2:
        if x[1] in log_in:
            print(1)
        else:
            print(0)
    else:
        log_in.discard(x[1])