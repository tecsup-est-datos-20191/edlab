'''

'''
from util.QueueLinkedLists import QueueLinkedListsCircular
from BinaryTreeNode import BinaryTreeNode

#
def levelOrder(root, result):

    if root is None:
        return

    q = QueueLinkedListsCircular()
    q.enQueue(root)
    nodeBT = None

    while not q.isEmpty():

        nodeBT = q.deQueue()      # dequeue FIFO
        #print(nodeBT.getData())
        result.append(nodeBT.getData())

        if nodeBT.getLeft():
            q.enQueue(nodeBT.getLeft())

        if nodeBT.getRight():
            q.enQueue(nodeBT.getRight())


# Resolution
#           A
#       B       C
#     D   E   F   G

nodeD = BinaryTreeNode(4)
nodeE = BinaryTreeNode(5)
nodeB = BinaryTreeNode(2,nodeD,nodeE)

nodeF = BinaryTreeNode(6)
nodeG = BinaryTreeNode(7)
nodeC = BinaryTreeNode(3,nodeF,nodeG)

nodeA = BinaryTreeNode(1,nodeB, nodeC)


#
result = [];
levelOrder(nodeA,result)
print(result)


#que = QueueLinkedListsCircular()
#que.enQueue("first")
#print("Front:" + que.queueFront())
#print("Rear:"+que.queueRear())

