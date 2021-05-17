from collections import deque
from sys import stdin, stdout


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if root is None:
                root = Node(data)
            elif root.data < data:
                root.right = self.insert(root.right, data)
            elif root.data > data:
                root.left = self.insert(root.left, data)
        return root

    def height(self, root):
        if root is None:
            return 0
        return max(1 + self.height(root.left), 1 + self.height(root.right))


arr = deque()
while True:
    x = [int(i) for i in stdin.readline().split()]
    if x == []:
        continue
    if x[0] == 0:
        arr.appendleft(x[1])
    elif x[0] == 1:
        arr.append(x[1])
    elif x[0] == 2:
        if x[1] in arr:
            arr.insert(arr.index(x[1]) + 1, x[2])
        else:
            arr.appendleft(x[2])
    else:
        break

T = BinaryTree()
for i in arr:
    T.insert(T.root, i)
print(T.height(T.root))