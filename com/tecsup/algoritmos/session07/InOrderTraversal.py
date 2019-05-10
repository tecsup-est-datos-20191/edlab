
from BinaryTreeNode import BinaryTreeNode

# In-order recursive traversal. The
# nodes' values are appended to the
# result list in traversal order
def inOrderRecursive(root, result):

    if not root:
        return

    inOrderRecursive(root.left, result)
    result.append(root.data)
    inOrderRecursive(root.right, result)


# In-order iterative traversal. The nodes'
# values are appended to the result list
# in traversal order
def inOrderIterative(root, result):

    if not root:
        return

    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node. left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)

root = BinaryTreeNode(1, childrenLeft, childrenRight)

result = []
inOrderRecursive(root, result)
print(result)

result = []
inOrderIterative(root, result)
print(result)