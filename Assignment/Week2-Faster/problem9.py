#Driver code
q = int(input())
for i in range(q):
    n = int(input())
    k = 0
    while (True):
        if ((n + k) % 2 == 0) and ( (n + k) / 2 >= 2):
            print(k)
            break
        k += 1
