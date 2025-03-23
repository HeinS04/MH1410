#U2421569C Hein San Lab02 T9
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0

    # find a node which contains the data matching the input value 
    def findNode(self, value): 
        curr = self.head
        while curr:
            if curr.data == value:
                return curr
            curr = curr.next 
        return curr 

    # add a new node as the first node      
    def addNode(self, data):
        newNode = Node(data)  # create the new node 
        newNode.next = self.head 
        self.head = newNode
        self.size+=1

    # print the data in all the nodes 
    def printNode(self):
        datalist = [] 
        curr = self.head
        while curr:
            datalist.append(curr.data)
            curr = curr.next 
        print(datalist)

    def copy(self):
        newlinkedlist = LinkedList()
        newlinkedlist.head = Node(self.head.data)
        currold = self.head.next
        currnew = newlinkedlist.head
        while currold:
            currnew.next = Node(currold.data)
            currnew = currnew.next
            currold = currold.next

        newlinkedlist.size = self.size
        return newlinkedlist
       
    
def copyLinkedList(linkedlistA):
    return linkedlistA.copy()


linkedlistA = LinkedList()
for i in range(1,6):
    linkedlistA.addNode(i)
linkedlistB = copyLinkedList(linkedlistA)
# modify linkedlistA
curr = linkedlistA.head
for i in range(linkedlistA.size):
    curr.data += 10
    curr = curr.next
linkedlistA.printNode()
linkedlistB.printNode()

