r,c = (int(i) for i in input().split())
arr = [[]]*r
max_ = [0]*c
for i in range(r):
    arr[i] = [(int(j)) for j in input().split()]
    for j in range(c):
        max_[j] = max(max_[j], len(str(arr[i][j])))
answer = ""
for i in arr:
    for j in range(c):
        answer += str(i[j]).rjust(max_[j],' ') + ' '
    answer += '\n'
print(answer)