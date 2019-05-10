
from util.QueueLinkedLists import QueueLinkedListsCircular
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


def findMaxUsingLevelOrder(root):

    maxElement = 0

    if root is None:
        return maxElement

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        if maxElement <=  nodeBT.getData() :
            maxElement = nodeBT.getData()

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return maxElement


#
# Resolution
#           A
#       B       C
#     D   E   F   G

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

#
findMaxRecursive(root)
print("findMaxRecursive: " + str(maxData))
#
max = findMaxUsingLevelOrder(root)
print("findMaxUsingLevelOrder : " + str(max))