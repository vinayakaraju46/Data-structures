class Node(object):
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None

class binarytree(object):
    def __init__(self):
        self.root = None

    def insert1(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftchild =  self.insertNode(data, node.leftchild)

        elif data > node.data:
            node.rightchild = self.insertNode(data, node.rightchild)

        return node

    def remove1(self, data):
        if not self.root:
            return
        else:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if data < node.data:
            if node.leftchild:
                node.leftchild = self.removeNode(data, node.leftchild)

        elif data > node.data:
            if node.rightchild:
                node.rightchild = self.removeNode(data, node.rightchild)

        else:
            if not node.rightchild and not node.leftchild:
                print("removing the leaf node...")
                del node
                return None
            if not node.rightchild:
                print("removing the node with one leftchild..")
                tempNode = node.leftchild
                del node
                return tempNode
            elif not node.leftchild:
                print("removing the node with one rightchild...")
                tempNode = node.rightchild
                del node
                return tempNode
            print("removing the node with two children...")
            tempNode = self.getPredeccor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removeNode(tempNode.data, node.leftchild)
        return node

    def getPredeccor(self, node):
        if node.rightchild:
            return self.getPredeccor(node.rightchild)
        return node

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)
    def traverseinorder(self, node):
        if node.leftchild:
            self.traverseinorder(node.leftchild)
        print("%d"%(node.data))

        if node.rightchild:
            self.traverseinorder(node.rightchild)
            
bst = binarytree()
bst.insert1(2)
bst.insert1(1)
bst.insert1(3)
bst.traverse()
bst.remove1(2)
bst.traverse()
