def Fibo(x):
    f = [0, 1]

    for i in range(2, x+1):
        a = f[i-1]
        b = f[i-2]
        f.append(a + b)
    
    return f[x]

x = int(input())
if (x < 1 or x > 30):
    print("So " + str(x) + " khong nam trong khoang [1,30].")
else:
    print(Fibo(x))