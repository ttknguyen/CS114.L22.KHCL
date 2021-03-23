from sys import stdin

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class bst:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if self.root is None:
            self.root = Node(val)
        else:
            if root is None:
                root = Node(val)
            elif root.val < val:
                root.right = self.insert(root.right, val)
            elif root.val > val:
                root.left = self.insert(root.left, val)
        return root
    
    def countLeaf(self, root):
        if (root == None): return 0
        if (root.left == None) and (root.right == None):
            return 1
        return self.countLeaf(root.left) + self.countLeaf(root.right)


tree = bst()
while True:
    try:
        a = int(stdin.readline())
        if (a != 0): tree.insert(tree.root, a)
        else: break
    except:
        continue    
print(tree.countLeaf(tree.root))