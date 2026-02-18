class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(node):
    if node is None:
        return
    print(node.data, end=",")
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data,end=",")
    inOrder(node.right)

def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data,end=",")

root = Tree("R")
nodeA = Tree("A")
nodeB = Tree("B")
nodeC = Tree("C")
nodeD = Tree("D")
nodeE = Tree("E")
nodeF = Tree("F")
nodeG = Tree("G")

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG

inOrder(root)

