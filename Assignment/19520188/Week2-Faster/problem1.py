n = input()
k = len(n)

ans = 0
for i in n: ans += int(i)**k

if (ans == int(n)):
    print(True)
else:
    print(False)
