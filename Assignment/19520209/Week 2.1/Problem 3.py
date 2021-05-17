a, b = list([int(i) for i in input().split()])
a_ = [int(i) for i in input().split()]
b_ = [int(i) for i in input().split()]

def merge_sorted_array(a_, b_, a, b):
    arr = []
    i = 0
    j = 0
    while(i < a and j < b):
        if a_[i] <= b_[j]:
            arr.append(a_[i])
            i += 1
        else:
            arr.append(b_[j])
            j += 1
    while(i < a):
        arr.append(a_[i])
        i += 1
    while(j < b):
        arr.append(b_[j])
        j += 1
    print(*arr)

merge_sorted_array(a_, b_, a, b)