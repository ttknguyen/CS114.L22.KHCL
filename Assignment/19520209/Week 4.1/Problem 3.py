# Link tham khảo: https://codereview.stackexchange.com/questions/179434/codefights-snake-game

heads = {'v': (1, 0),
         '^': (-1, 0),
         '<': (0, -1),
         '>': (0, 1)
         }

new_direc = {'v': {'L': '>', 'R': '<'},
             '^': {'L': '<', 'R': '>'},
             '<': {'L': 'v', 'R': '^'},
             '>': {'L': '^', 'R': 'v'}
             }

def find_snake(gameBoard):
    def get_next(x, y):
        for key, direc in heads.items():
            new_x, new_y = x + direc[0], y + direc[1]
            if (new_x in range(len(gameBoard)) and new_y in range(len(gameBoard[0]))):
                if ((new_x, new_y) not in snake):
                    if gameBoard[new_x][new_y] == '*':
                        return (new_x, new_y)
        return None

    # Get the head and the next body opposite of snake's direction
    snake = []
    for i, row in enumerate(gameBoard):
        for head in heads:
            if head in row:
                snake.append((i, row.index(head)))
                # snake.append((snake[0][0] + typeHeads[head][0] * -1, snake[0][1]  + typeHeads[head][1] * -1))

    # Append the rest of the body
    while True:
        n = get_next(snake[-1][0], snake[-1][1])
        if n is None:
            break
        snake.append(n)
    return snake

def move_snake(gameBoard, snake):
    head = gameBoard[snake[0][0]][snake[0][1]]
    new_x, new_y = snake[0][0] + heads[head][0], snake[0][1] + heads[head][1]
    new_snake = []
    if new_x in range(len(gameBoard)) and new_y in range(len(gameBoard[0])) and (new_x, new_y) not in snake:
        new_snake.append((new_x, new_y))

        for pos in snake[:-1]:
            new_snake.append(pos)

        return new_snake

# Find starting snake
def snakeGame(gameBoard, snake, commands):
    for command in commands:
        if command in "LR":
            # Change the head
            gameBoard[snake[0][0]][snake[0][1]] = new_direc[gameBoard[snake[0][0]][snake[0][1]]][command]
        else:
            temp = move_snake(gameBoard, snake)

            # if not valid move return dead snake
            if temp is None:
                for pos in snake:
                    x, y = pos
                    gameBoard[x][y] = 'X'
                return gameBoard

            # else move snake
            for a, b in zip(snake, temp):
                gameBoard[b[0]][b[1]] = gameBoard[a[0]][a[1]]

            gameBoard[snake[-1][0]][snake[-1][1]] = '.'
            snake = temp

n, m, c = list([int(i) for i in input().split()])
gameBoard = []
for i in range(n):
    temp = [i for i in input()]
    gameBoard.append(temp)
snake = find_snake(gameBoard)
commands = input()
gameBoard = snakeGame(gameBoard, snake, commands)
for i in range(n):
    for j in range(m):
        print(*gameBoard[i][j], end="")
    print()

# Link tham khảo: https://codereview.stackexchange.com/questions/179434/codefights-snake-game