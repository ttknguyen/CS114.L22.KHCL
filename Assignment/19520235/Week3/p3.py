from sys import exec_prefix, stdin, stdout
from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def Insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = Insert(root.right, key)
        else:
            root.left = Insert(root.left, key)
    return root

def Height(root):
    if root is None:
        return 0 
    else:
        leftHeight = Height(root.left)
        rightHeight = Height(root.right)
        if (leftHeight > rightHeight):
            return leftHeight + 1
        else:
            return rightHeight + 1

# create a list
queue = deque()
while True:
    try:
        li = [int(i) for i in stdin.readline().split()]
        if li[0] == 3: break
        if li[0] == 0: queue.appendleft(li[1])
        if li[0] == 1: queue.append(li[1])
        else:
            try:
                queue.insert(queue.index(li[1]) + 1, li[2])
            except:
                queue.appendleft(li[2])
    except:
        continue

# create a binary tree
isRoot = True
while True:
    try:
        if isRoot: 
            root = Node(queue.popleft())
            isRoot = False
        else:
            root = Insert(root, queue.popleft())
    except:
        break
print(Height(root))