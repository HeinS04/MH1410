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

     # Reverse the linked list in-place
    def reverse(self): [1,2,3,4]
        prev = None
        curr = self.head 
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr 
            curr = next_node 
        self.head = prev

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


linkedlistA = LinkedList()
for i in range(1,6):
    linkedlistA.addNode(i)
linkedlistA.printNode()
linkedlistA.reverse()
print("After reversing the linked list, the linked list becomes:")
linkedlistA.printNode()

