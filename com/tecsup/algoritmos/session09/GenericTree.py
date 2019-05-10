########################################
#       Generic Tree
########################################
class TreeNode:

    #Constructor
    def __init__(self, data=None):
        self.data = data
        self.firstChild = None
        self.nextSibling = None

def findSum(root):
    if(root == None):
        return 0
    return root.data + findSum(root.firstChild) + findSum(root.nextSibling)

def findMul(root):
    if(root == None):
        return 1
    return root.data * findMul(root.firstChild) * findMul(root.nextSibling)

# programa principal
#
#      A
#    / \ \
#    | |  |
#    B C  D
#      |
#      |
#      G
if __name__ == '__main__':

    nodeA = TreeNode(1)
    nodeB = TreeNode(2)
    nodeC = TreeNode(3)
    nodeD = TreeNode(4)
    nodeG = TreeNode(7)

    nodeA.firstChild = nodeB
    nodeB.nextSibling = nodeC
    nodeC.nextSibling = nodeD
    nodeC.firstChild = nodeG

    # Suma
    print(findSum(nodeA))
    print(findMul(nodeA))