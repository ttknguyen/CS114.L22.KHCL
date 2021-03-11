class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Print(self):
        tmp = self.head
        while tmp is not None:
            print(str(tmp.dataval), end = " ")
            tmp = tmp.nextnode
        print()

    def AddHead(self, newData):

        if (self.head is None):
            self.head = Node(newData)
            return

        newNode = Node(newData)
        newNode.nextnode = self.head
        self.head = newNode

    def AddEnd(self, newData):
        newNode = Node(newData)

        if (self.head is None):
            self.head = newNode
            return

        last = self.head
        while (last.nextnode):
            last = last.nextnode
        last.nextnode = newNode
    
    def AddAB(self, A, B):
        newNode = Node(B)
        
        tmp = self.head
        while (tmp is not None):
            if (tmp.dataval == A):
                newNode.nextnode = tmp.nextnode
                tmp.nextnode = newNode
                return
            tmp = tmp.nextnode

        self.AddHead(B)

    def DeleteHead(self):
        tmp = self.head
        self.head = tmp.nextnode
     

    def DeleteA(self, A):
        tmp = self.head

        if (tmp.dataval == A):
            self.DeleteHead()
            return True

        while (tmp.nextnode):
            if (tmp.nextnode.dataval == A):
                tmp2 = tmp.nextnode
                tmp.nextnode = tmp2.nextnode
                return True

            tmp = tmp.nextnode
            
        return False

    def DeleteAllA(self, A):
        check = True
        while (check):
            check = self.DeleteA(A)
            

#Driver Code
llist = LinkedList()
while (True):
    inp = [int(i) for i in input().split()]
    if (inp[0] == 0):
        llist.AddHead(inp[1])
    elif (inp[0] == 1): 
        llist.AddEnd(inp[1])
    elif (inp[0] == 2): 
        llist.AddAB(inp[1], inp[2])
    elif (inp[0] == 3): 
        llist.DeleteA(inp[1])
    elif (inp[0] == 4): 
        llist.DeleteAllA(inp[1])
    elif (inp[0] == 5): 
        llist.DeleteHead()
    elif (inp[0] == 6): break

if (llist.head == None):
    print("blank")
else:
    llist.Print()


