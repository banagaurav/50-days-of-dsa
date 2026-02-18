class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def travers(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next

    print("null")

def insert_to_position(head,newNode,position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head

    for _ in range(position-2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode

    return head

def delete_node(head,nodeToDelete):
    if nodeToDelete == head:
        return head.next
    
    currentNode = head
    
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next == None:
        return head
    
    currentNode.next == currentNode.next.next

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4




