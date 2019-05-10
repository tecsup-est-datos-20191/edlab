from queue import Queue
from ASTTreeTraversal import PlusNode, TimesNode, NumNode
def E(q):
    if q.isEmpty():
        raise ValueError("Invalid Prefix Expression")
    token = q.dequeue()
    if token == "+":
        return PlusNode(E(q),E(q))
    if token == "*":
        return TimesNode(E(q),E(q))
    return NumNode(float(token))

def main():

    #x = input("Please enter a prefix expression: ")
    x = " + 1 5"
    lst = x.split()
    q = Queue()
    print(lst)

    for token in lst:
        q.enqueue(token)

    print(q)

    root = E(q)
    print(root)

    print(root.eval())
    print(root.inorder())

if __name__ == '__main__':
    main()