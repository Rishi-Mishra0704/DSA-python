class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def printList(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

def reverseList(head):
    current = head
    prev = None
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    # Update the head to the new first node (previously the last node)
    return prev

print("Original")
printList(a)

print("Reversed")
new_head = reverseList(a)
printList(new_head)
