from sys import stdin, stdout
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
 
def LevelOrder(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while(len(queue) > 0):
        stdout.write(str(queue[0].data) + " ")
        node = queue.popleft()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

# main
isRoot = True
while True:
    data = int(stdin.readline())
    if data == 0: break
    if isRoot: 
        root = Node(data)
        isRoot = False
    else: root = Insert(root, data)
LevelOrder(root)