class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class linkedlist(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = self.tail = Node(data)

        else:
            newNode.nextNode = self.head
            self.head.prevNode = newNode
            self.head = newNode
        return self.head    

    def reverse(self):
        temp = None
        curr = self.head
        while curr:
            temp = curr.prevNode
            curr.prevNode = curr.nextNode
            curr.nextNode = temp
            curr = curr.prevNode
        if temp is not None:
            self.head = temp.prevNode

        return self.head
    
    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d"%(actualNode.data))
            actualNode = actualNode.nextNode

ll = linkedlist()
n = int(input("Enter the no. of elements..."))
for i in range(n):
    ll.insert(int(input()))

   
ll.traverse()
print('\n')
ll.reverse()
ll.traverse()
