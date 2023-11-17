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
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

# Example usage
inorder_traversal(root)
# Output: 4 2 5 1 3
