class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# Write a fucntion to find the target value in the linked list
def findVal(head, x):
    current = head
    if current == None:
        return None

    while current is not None:
        if current.val == x:
            return current.val
        else:
            current = current.next



result = findVal(a, "c")
print(result)