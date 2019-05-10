
from util.QueueLinkedLists import QueueLinkedListsCircular
from BinaryTreeNode import BinaryTreeNode

def sumRecursive(root):
    if (root == None):
        return 0
    return root.data + \
           sumRecursive(root.left) + \
           sumRecursive(root.right)



def sumUsingLevelOrder(root):

    sum = 0

    if root is None:
        return sum

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        sum += nodeBT.getData()

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return sum


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

tmp = sumRecursive(root)
print("La suma del arbol es %d" % (tmp))

tmp2 = sumUsingLevelOrder(root)
print("La suma del arbol es %d" % (tmp2))