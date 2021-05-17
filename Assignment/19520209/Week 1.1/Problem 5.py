k, t = list([int(i) for i in input().split()])

def train(k, t):
    p = t // k
    t = t % k
    if p % 2 == 0:
        return t
    return k - t

print(train(k, t))