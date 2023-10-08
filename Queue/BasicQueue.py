class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def peek(self):
        if self.items:
            return self.items[0]
        return None
    
    def is_empty(self):
        if self.items == []:
            return "Queue is empty"
        return "Queue is not empty" 
    


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)
print(queue.dequeue())
print(queue.dequeue())
print(queue.items)
print(queue.peek())
print(queue.is_empty())
queue.enqueue(4)
print(queue.items)