class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
        print(f"{element} is push into stack")

    def pop(self):
        if self.isEmpty():
            print('stack is empty')
        self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print('stack is empty')
        return self.stack[-1]
    

myStack = Stack()

myStack.push(5)
print("Peek: ", myStack.peek())
