DIR = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}

FLOW = {
        'l': {'2': 'l', '3': 'd', '6': 'u', '7': 'l'},
        'r': {'2': 'r', '4': 'd', '5': 'u', '7': 'r'},
        'd': {'1': 'd', '5': 'l', '6': 'r', '7': 'd'},
        'u': {'1': 'u', '3': 'r', '4': 'l', '7': 'u'}
}

RANGE = lambda x, y, state: 0 <= x < len(state) and 0 <= y < len(state[0])

def StartPoint(state):
    pipes = list(filter(lambda x: 'a' <= x <= 'z',''.join(state)))
    starts = {}
    for i in range(len(state)):
        for j in range(len(state[0])):
            if 'a'<=state[i][j]<='z':
                starts[state[i][j]] = [i,j]
    return starts, pipes

def Flow(flow, cur_path, state, end, final_path):
    x, y = [x+y for x,y in zip(cur_path[-1], DIR[flow])]
    if RANGE(x, y, state) and state[x][y] == end:
        final_path.append(cur_path + [''])
    elif RANGE(x, y, state) and state[x][y] in FLOW[flow]:
        return Flow(FLOW[flow][state[x][y]], cur_path + [[x, y]], state, end, final_path)
    else:
        final_path.append(cur_path + ['leak'])
    return final_path

def Sum(total_path):
    final_cells = set()
    first_leak = list(map(lambda x: len(x), filter(lambda x: 'leak' in x, total_path)))
    first_leak = 0 if len(first_leak) == 0 else min(first_leak) - 1
    for path in total_path:
        path = path[:-1]
        path = list(map(lambda x: str(x[0]) + ' ' + str(x[1]), path))
        idx = min(first_leak, len(path)) if first_leak else len(path)
        final_cells |= set(path[:idx])
    return len(final_cells) * (-1 if first_leak > 0 else 1)

def Solve(state):
    starts, pipes = StartPoint(state)
    total_path = []
    for pipe in pipes:
        end = pipe.upper()
        for di in DIR:
            x, y = [x+y for x,y in zip(starts[pipe], DIR[di])]
            if RANGE(x, y, state) and state[x][y] in FLOW[di]:
                total_path += Flow(FLOW[di][state[x][y]], [[x, y]], state, end, [])
    return Sum(total_path)

n = int(input())
state = []
for i in range(n):
    state.append(input())

print(Solve(state))