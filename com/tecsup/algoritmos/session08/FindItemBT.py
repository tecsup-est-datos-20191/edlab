
from util.QueueLinkedLists import QueueLinkedListsCircular
from BinaryTreeNode import BinaryTreeNode

#
def findDataRecursive(root, dataSearch):

    if not root :
        return 0

    if root.getData() == dataSearch:
        return 1
    else:
        tmp = findDataRecursive(root.left, dataSearch)
        if tmp == 1 :
            return tmp
        else:
            return findDataRecursive(root.right, dataSearch)

#
def findDataUsingLevelOrder(root, dataSearch):

    flag = 0

    if root is None:
        return flag

    q = QueueLinkedListsCircular()
    q.enQueue(root)

    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()  # dequeue FIFO

        if dataSearch ==  nodeBT.getData() :
            flag = 1

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())

    return flag


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

dataSearch = 7
tmp = findDataRecursive(root, dataSearch)
print("Se encontro el valor de %d, %d vez" % (dataSearch, tmp))

tmp2 = findDataUsingLevelOrder(root, dataSearch)
print("Se encontro el valor de %d, %d vez" % (dataSearch, tmp2))