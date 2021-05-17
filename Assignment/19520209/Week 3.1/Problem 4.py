from sys import stdin, stdout
class Node:
    def __init__(self, data, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if root is None:
                root = Node(data)
            elif root.data < data:
                root.right = self.insert_node(root.right, data)
            elif root.data > data:
                root.left = self.insert_node(root.left, data)
        return root

    def count(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count(root.left) + self.count(root.right)

T = BinaryTree()
while True:
    x = [int(i) for i in stdin.readline().split()]
    if len(x) == 0:
        continue
    if x[0] == 0:
        break
    T.insert_node(T.root, x[0])
print(T.count(T.root))