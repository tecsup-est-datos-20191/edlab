
from util.QueueLinkedLists import QueueLinkedListsCircular
from BinaryTreeNode import BinaryTreeNode

def getSizeRecursive(root):

    if not root :
        return 0

    return getSizeRecursive(root.left) + \
           getSizeRecursive(root.right) + 1


def getSizeUsingLevelOrder(root):

    count = 0

    if root is None:
        return count

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        count += 1

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return count

#
# Resolution
#           A
#       B       C
#     D   E   F   G

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)


tmp = getSizeRecursive(root)
print("el tamaño del arbol es %d" % (tmp))

tmp2 = getSizeUsingLevelOrder(root)
print("el tamaño del arbol es %d" % (tmp2))