from BinaryTreeNode import BinaryTreeNode

maxData = float("-infinity")

def findMaxRecursive(root):

    global maxData
    if not root:
        return maxData

    if root.getData() > maxData:
        maxData = root.getData()

    findMaxRecursive(root.getLeft())
    findMaxRecursive(root.getRight())

    return maxData

childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)

root = BinaryTreeNode(1,childrenLeft,childrenRight)

findMaxRecursive(root)
print(maxData)