class Node(object):
    def __init__(self,character):
        self.character = character
        self.leftchild = None
        self.rightchild = None
        self.middlechild = None
        self.value = 0

class TernaryTree(object):

    def __init__(self):
        self.root = None

    def put(self,key,value):
        self.root = self.putItem(self.root,key,value,0)

    def putItem(self,node,key,value,index):

        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.leftchild = self.putItem(node.leftchild,key,value,index)

        elif c > node.character:
            node.rightchild = self.putItem(node.rightchild,key,value,index)

        elif index < len(key) - 1 :
            node.middlechild = self.putItem(node.middlechild,key,value,index+1)

        else:
            node.value = value

        return node

    def get(self,key):

        node = self.getItem(self.root,key,0)

        if node == None:
            return -1
        return node.value

    def getItem(self,node,key,index):


        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftchild,key,index)

        elif c > node.character: 
            return self.getItem(node.rightchild,key,index)

        elif index < len(key) - 1 :
            return self.getItem(node.middlechild,key,index+1)

        else:
            return node

if __name__ == "__main__":
    Tt = TernaryTree()
    Tt.put("vinay",406)
    Tt.put("rahulmk",98)
    print(Tt.get("vinay"))
