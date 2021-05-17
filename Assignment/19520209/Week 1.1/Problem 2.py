x = int(input())

def Fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return Fibo(x-1) + Fibo(x-2)

if x < 1 or x > 30:
    print('So', x, 'khong nam trong khoang [1,30].')
else:
    print(Fibo(x))