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
    def print_level(self, root, height, h):
        if root is None: return 0
        if h == height:
            print(root.data, end=' ')
        self.print_level(root.left, height, h + 1)
        self.print_level(root.right, height, h + 1)

T = BinaryTree()
while True:
    x = [int(i) for i in stdin.readline().split()]
    if x == []:
        continue
    if x[0] == 0:
        break
    T.insert(T.root, x[0])
height = T.height(T.root)
for i in range(height):
    T.print_level(T.root, i, 0)