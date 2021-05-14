server = set()

while True:
    code = [int(i) for i in input().split()]
    if code[0] == 0: break
    elif code[0] == 1:
        server.add(code[1])
    else:
        if code[1] in server:
            print(1)
        else:
            print(0)