class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

'''
    1
   / \
  2   3
 / \
4   5

'''
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")

# Example usage
postorder_traversal(root)
# Output: 4 5 2 3 1
