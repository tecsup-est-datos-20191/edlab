
from BinaryTreeNode import BinaryTreeNode


# Pre-order recursivc traversal.
# The nodes' values are appended to
# the result list in traversal order
def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)

# Pre-order iterative traversal. The nodes'
# values arc appended to the result list
# in traversal order
def preOrderIterative(root, result):

    if not root:
        return

    stack = []
    stack.append(root)

    while stack:

        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)
root = BinaryTreeNode(1,childrenLeft,childrenRight )


result = []
preOrderRecursive(root, result)
print(result)

#result = []
#preOrderIterative(root, result)
#print(result)