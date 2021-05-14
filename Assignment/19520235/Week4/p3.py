snake = []
HEADS = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}
DIR = {
    'v': { 'L':'>', 'R':'<'},
    '^': { 'L':'<', 'R':'>'},
    '<': { 'L':'v', 'R':'^'},
    '>': { 'L':'^', 'R':'v'} 
}

def FindHead(board):
    for i, row in enumerate(board):
        for head in HEADS:
            if head in row:
                return (i, row.index(head))

def GetBody(x, y, board):
    for dim in HEADS.values():
        x_new, y_new = x + dim[0], y + dim[1]
        if x_new in range(len(board)) and y_new in range(len(board[0])) \
            and (x_new, y_new) not in snake \
            and board[x_new][y_new] == '*':
                return (x_new, y_new)

def SnakeShape(board):
    global snake
    snake.append(FindHead(board))
    while True:
        pos = GetBody(snake[-1][0], snake[-1][1], board)
        if pos == None: 
            break
        snake.append(pos)
    return snake

def checkDieSnake(board, newHeadPoint):
    global snake
    if newHeadPoint in snake[:-1] or newHeadPoint[0] < 0 or newHeadPoint[1] < 0 \
        or newHeadPoint[0] > len(board) - 1 or newHeadPoint[1] > len(board[0]) - 1:
            for point in snake:
                board[point[0]][point[1]] = 'X'
            for i in board:
                print(*i, sep = "")
            exit()
    return

def Control(board, cmd_str):
    global snake
    snake = SnakeShape(board)
    for command in cmd_str:
        headPoint = snake[0]
        if command in "LR":
            board[headPoint[0]][headPoint[1]] = DIR[board[headPoint[0]][headPoint[1]]][command]
        else:
            newHeadPoint = (-1, -1)
            if board[headPoint[0]][headPoint[1]] == "^":
                newHeadPoint = (headPoint[0] - 1, headPoint[1])
            if board[headPoint[0]][headPoint[1]] == "<":
                newHeadPoint = (headPoint[0], headPoint[1] - 1)
            if board[headPoint[0]][headPoint[1]] == "v":
                newHeadPoint = (headPoint[0] + 1, headPoint[1])
            if board[headPoint[0]][headPoint[1]] == ">":
                newHeadPoint = (headPoint[0], headPoint[1] + 1)
            checkDieSnake(board, newHeadPoint)
            # in case snake only has head and tail => snake never die!!!
            if newHeadPoint == snake[-1]:
                snake.insert(0, newHeadPoint)
                board[newHeadPoint[0]][newHeadPoint[1]] = board[headPoint[0]][headPoint[1]]
                board[headPoint[0]][headPoint[1]] = '*'
                snake.pop()
            else:
                snake.insert(0, newHeadPoint)
                lastPoint = snake.pop()
                board[newHeadPoint[0]][newHeadPoint[1]] = board[headPoint[0]][headPoint[1]]
                board[headPoint[0]][headPoint[1]] = '*'
                board[lastPoint[0]][lastPoint[1]] = '.'
    return board

n, m, c = [int(i) for i in input().split()]
board = []
for i in range(n):
    row = [i for i in input()]
    board.append(row)
cmd_str = input()

board = Control(board, cmd_str)
for i in range(n):
    for j in range(m):
        print(*board[i][j], end = "")
    print()