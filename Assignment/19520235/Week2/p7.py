from sys import stdin, stdout
server = set()

while True:
    try:
        code = [int(i) for i in stdin.readline().split()]
        if code[0] == 0: break
        elif code [0] == 1:
            server.add(code[1])
        elif code[0] == 3:
            server.discard(code[1])
        else:
            stdout.write(str(int(code[1] in server)) + '\n')
    except:
        exit()