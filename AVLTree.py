class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftchild = None
        self.rightchild = None

class Avltree(object):
    def __init__(self):
        self.root = None

    def calcheight(self, node):
        if not node:
            return -1
        return node.height

    def calcbalance(self, node):
        if not self.root:
            return 0
        return self.calcheight(node.leftchild) - self.calcheight(node.rightchild)


    def insert1(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftchild = self.insertNode(data, node.leftchild)
        else:
            node.rightchild = self.insertNode(data, node.rightchild)

        node.height = max(self.calcheight(node.leftchild), self.calcheight(node.rightchild)) + 1

        return self.settleViolation(data, node)

    def remove1(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.leftchild = self.removeNode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removeNode(data, node.rightchild)
        else:
            if not node.rightchild and not node.leftchild:
                print("removing the leaf node...")
                del node
                return None
            if not node.leftchild:
                print("removing the node with one rightchild")
                tempNode = node.rightchild
                del node
                return tempNode
            elif not node.rightchild:
                print("removing the node with one leftchild")
                tempNode = node.leftchild
                del node
                return tempNode
            print("removing the node with two children...")
            tempNode = self.getPredeccor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removeNode(tempNode.data, node.leftchild)

        if not node:
            return node
        node.height = max(self.calcheight(node.leftchild), self.calcheight(node.rightchild)) + 1

        balance = self.calcbalance(node)

        if balance > 1 and self.calcbalance(node.leftchild) >= 0:
            return self.rotateright(node)

        if balance > 1 and self.calcbalance(node.leftchild) < 0:
            node.leftchild = self.rotateleft(node.leftchild)
            return self.rotateright(node)

        if balance < -1 and self.calcbalance(node.rightchild) <= 0:
            return self.rotateleft(node)

        if balance < -1 and self.calcbalance(node.rightchild) >= 0:
            node.rightchild = self.rotateright(node.rightchild)
            return self.rotateleft(node)
        return node

    def getPredeccor(self, node):
        if node.rightchild:
            return self.getPredeccor(node.leftchild)
        return node     
    

    def settleViolation(self, data, node):
        balance = self.calcbalance(node)

        if balance > 1 and data < node.leftchild.data:
            print("Left Left heavy situation...")
            return self.rotateright(node)
        if balance < -1 and data > node.rightchild.data:
            print("Right Right heavy situation..")
            return self.rotateleft(node)
        if balance > 1 and data > node.leftchild.data:
            print("Left Right heavy situation..")
            node.leftchild = self.rotateleft(node.leftchild)
            return self.rotateright(node)
        if balance < -1 and data < node.rightchild.data:
            print("Right Left heavy situation..")
            node.rightchild = self.rotateright(node.rightchild)
            return self.rotateleft(node)

        return node
            
        

    def rotateright(self, node):
        tempLeftchild = node.leftchild
        t = tempLeftchild.rightchild

        tempLeftchild.rightchild = node
        node.leftchild = t

        node.height= (max(self.calcheight(node.leftchild), self.calcheight(node.rightchild))) + 1
        tempLeftchild.height = (max(self.calcheight(tempLeftchild.leftchild), self.calcheight(tempLeftchild.rightchild))) + 1

        return tempLeftchild

    def rotateleft(self, node):
        tempRightchild = node.rightchild
        t = tempRightchild.leftchild

        tempRightchild.leftchild = node
        node.rightchild = t

        node.height = (max(self.calcheight(node.leftchild), self.calcheight(node.rightchild))) + 1
        tempRightchild.height = (max(self.calcheight(tempRightchild.leftchild), self.calcheight(tempRightchild.rightchild))) + 1

        return tempRightchild

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)

    def traverseinorder(self, node):
        if node.leftchild:
            self.traverseinorder(node.leftchild)

        print("%d"%(node.data))

        if node.rightchild:
            self.traverseinorder(node.rightchild)

avl = Avltree()
avl.insert1(12)
avl.insert1(2)
avl.insert1(1)
avl.insert1(3)
avl.insert1(54)
avl.traverse()

avl.remove1(12)

avl.traverse()
            
