class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None
    

class linkedlist(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def insertion(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode     

    def endinsertion(self, data):
       self.size = self.size + 1
       newNode = Node(data)
       actualNode = self.head

       while actualNode.nextNode is not None:
           actualNode = actualNode.nextNode

       actualNode.nextNode = newNode

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            n = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = n
        self.head = prev

    def deletion(self):
        if not self.head:
           return

        else:
            self.size = self.size - 1
            currentNode = self.head
            previousNode = None

            while currentNode.data != previousNode.data:
                previousNode = currentNode
                currentNode = currentNode.nextNode

            if previousNode is None:
                self.head = currentNode.nextNode

            else:
                previousNode.nextNode = currentNode.nextNode

    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d"%(actualNode.data))
            actualNode = actualNode.nextNode
            
link = linkedlist()  
N = int(input("Enter the no. of elements...")
for i in range(N):
    link.insert(int(input())
link.endinsertion(int(input())
link.traverse()
print('\n')
link.reverse()
link.traverse()
    
    
