from sys import stdin, stdout

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
 
def CountLeaf(root):
    if root is None:
        return 0 
    if(root.left is None) and (root.right is None):
        return 1 
    else:
        return CountLeaf(root.left) + CountLeaf(root.right)

# main
isInit = False
while True:
    data = int(stdin.readline())
    if data == 0: break
    if isInit == False: 
        root = Node(data)
        isInit = True
    else: root = Insert(root, data)
print(CountLeaf(root))