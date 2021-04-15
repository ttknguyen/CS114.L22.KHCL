
typeHeads = {
    'v': (1, 0),
    '^': (-1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

direc = {
    'v': { 'L':'>', 'R':'<'},
    '^': { 'L':'<', 'R':'>'},
    '<': { 'L':'v', 'R':'^'},
    '>': { 'L':'^', 'R':'v'} 
}

def findSnake(board):
    snake = []

    def dfs(x, y):
        #print(x, y, snake)
        for step, d in typeHeads.items():
            newX, newY = x + d[0], y + d[1]
            if (newX in range(len(board)) and newY in range(len(board[0]))):
                #print(newX, newY, d)
                if ((newX, newY) not in snake):
                    #print(newX, newY, 'alo')
                    if (board[newX][newY] == '*'):
                        #print(newX, newY)
                        return (newX, newY)
        return None

    for i, row in enumerate(board):
        for head in typeHeads:
            if head in row:
                snake.append((i, row.index(head)))
                #snake.append((snake[0][0] + typeHeads[head][0] * -1, snake[0][1]  + typeHeads[head][1] * -1))

    while True:
        pos = dfs(snake[-1][0], snake[-1][1])
        if (pos == None):
            break
        snake.append(pos)
    return snake

def moveSnake(board, snake):
    head = board[snake[0][0]][snake[0][1]]
    newHeadX = snake[0][0] + typeHeads[head][0]
    newHeadY = snake[0][1] + typeHeads[head][1]

    if (newHeadX not in range(len(board))):
        return None
    if (newHeadY not in range(len(board[0]))):
        return None
    if ((newHeadX,newHeadY) in snake[:-1]):
        return None
    
    newSnake = [(newHeadX,newHeadY)]
    for i in range(len(snake)-1):
        newSnake.append(snake[i])
    return newSnake

def control(board, snake, listStep):
    for step in listStep:
        if (step == 'L' or step == 'R'):
            x, y = snake[0][0], snake[0][1]
            board[x][y] = direc[board[x][y]][step]
        else:
            tmp = moveSnake(board, snake)

            if tmp is None:
                for i in snake:
                    board[i[0]][i[1]] = 'X'
                return board

            if (tmp[0] == snake[-1]) and (len(tmp) == 2):
                board[tmp[0][0]][tmp[0][1]] = board[snake[0][0]][snake[0][1]]
                board[tmp[1][0]][tmp[1][1]] = '*'
                snake = tmp
            else:
                for a, b in zip(snake, tmp):
                    board[b[0]][b[1]] = board[a[0]][a[1]]
                board[snake[-1][0]][snake[-1][1]] = '.'
                snake = tmp

    return board

''' DRIVER CODE  '''
m, n, c = list([int(i) for i in input().split()])
board = []
for i in range(m):
    tmp = [i for i in input()]
    board.append(tmp)
snake = findSnake(board)
#print(snake)
listStep = input()
board = control(board, snake, listStep)
for i in range(m):
    for j in range(n):
        print(*board[i][j], end = "")
    print()