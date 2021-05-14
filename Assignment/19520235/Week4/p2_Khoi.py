from sys import stdin
import heapq as heap
n = int(input())
board = []
while len(board) != n:
    temp = list(stdin.readline().split())
    if temp == []: continue
    board += temp
def turn_left(state, x, y):
    if state == 'Up':
        return 'Left', x, y-1
    if state == 'Down':
        return 'Right', x, y+1
    if state == 'Left':
        return 'Down', x+1, y
    if state == 'Right':
        return 'Up', x-1, y
def turn_right(state, x, y):
    if state == 'Up':
        return 'Right', x, y+1
    if state == 'Down':
        return 'Left', x, y-1
    if state == 'Left':
        return 'Up', x-1, y
    if state == 'Right':
        return 'Down', x+1, y
def forward(state, x, y):
    if state == 'Up':
        return 'Up', x-1, y
    if state == 'Down':
        return 'Down', x+1, y
    if state == 'Left':
        return 'Left', x, y-1
    if state == 'Right':
        return 'Right', x, y+1
def find_start():
    start = {}
    for i in board:
        for j in i:
            if 'a' <= j <= 'z':
                start[j] = (board.index(i), i.index(j))
    return start
def legal_move(x,y):
    if x < 0 or x >= n or y < 0 or y >= len(board[0]):
        return False
    if board[x][y] == '0':
        return False
    return True
def find_intersect(cross, intersect, temp):
    if len(cross) == 0:
        for x in temp:
            cross += (x,)
    else:
        for x in temp:
            if x in cross:
                intersect.append(x)
            else:
                cross +=(x,)
    return cross, intersect
def move(state,x,y,count,cross):
    if not legal_move(x,y):
        return count, 'YES', cross
    if 'A' <= board[x][y] <= 'Z':
        return count, 'NO', cross
    if state == 'Up':
        if board[x][y] in ['1', '7']:
            if board[x][y] == '7':
                cross.append((x,y))
            state,x,y = forward(state,x,y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['3']:
            state,x,y = turn_right(state,x,y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['4']:
            state,x,y = turn_left(state,x,y)
            return move(state, x, y, count + 1,cross)
        else:
            return count, 'YES', cross
    if state == 'Down':
        if board[x][y] in ['1', '7']:
            if board[x][y] == '7':
                cross.append((x,y))
            state, x, y = forward(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['5']:
            state, x, y = turn_right(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['6']:
            state, x, y = turn_left(state, x, y)
            return move(state, x, y, count + 1,cross)
        else:
            return count, 'YES', cross
    if state == 'Left':
        if board[x][y] in ['2', '7']:
            if board[x][y] == '7':
                cross.append((x,y))
            state, x, y = forward(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['6']:
            state, x, y = turn_right(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['3']:
            state, x, y = turn_left(state, x, y)
            return move(state, x, y, count + 1,cross)
        else:
            return count, 'YES', cross
    if state == 'Right':
        if board[x][y] in ['2', '7']:
            if board[x][y] == '7':
                cross.append((x,y))
            state, x, y = forward(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['4']:
            state, x, y = turn_right(state, x, y)
            return move(state, x, y, count + 1,cross)
        if board[x][y] in ['5']:
            state, x, y = turn_left(state, x, y)
            return move(state, x, y, count + 1,cross)
        else:
            return count, 'YES', cross
def game():
    start = find_start()
    no_leaks = []
    leaks = []
    intersect = []
    cross = ()
    for i in start.values():
        pipe, leak, temp = move('Up',i[0]-1,i[1],0,[])
        if pipe != 0:
            cross, intersect = find_intersect(cross, intersect, temp)
            if leak == 'YES':
                leaks.append(pipe)
            else:
                no_leaks.append(pipe)
        pipe, leak, temp = move('Down', i[0]+1, i[1],0,[])
        if pipe != 0:
            cross, intersect = find_intersect(cross, intersect, temp)
            if leak == 'YES':
                leaks.append(pipe)
            else:
                no_leaks.append(pipe)
        pipe, leak, temp = move('Left', i[0], i[1]-1,0,[])
        if pipe != 0:
            cross, intersect = find_intersect(cross,intersect,temp)
            if leak == 'YES':
                leaks.append(pipe)
            else:
                no_leaks.append(pipe)
        pipe, leak, temp = move('Right', i[0], i[1]+1,0,[])
        if pipe != 0:
            cross, intersect = find_intersect(cross,intersect,temp)
            if leak == 'YES':
                leaks.append(pipe)
            else:
                no_leaks.append(pipe)
    if leaks == []:
        return sum(no_leaks) - len(intersect)
    else:
        leak = min(leaks)
        for j in range(len(no_leaks)):
            if no_leaks[j] > leak:
                no_leaks[j] = leak
        return -1*(sum(no_leaks) + leak*len(leaks))
print(game())