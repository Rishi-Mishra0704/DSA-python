class Stack:
    # initialize the stack
    def __init__(self):
        self.stack = []

    # push an item onto the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the stack
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    # get the top item from the stack
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    # check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # get the size of the stack
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())
print("Popped element:", stack.pop())

print("Stack size:", stack.size())
print("Top element:", stack.peek())
