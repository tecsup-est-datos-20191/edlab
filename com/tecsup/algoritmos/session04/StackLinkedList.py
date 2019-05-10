'''
Created on Mar 11, 2019
@author: jgomezm
'''
# Node of a Single Linked List
class Node(object):

    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the data
    def setNext(self, next):
        self.next = next

    # Method for getting the data
    def getNext(self):
        return self.next

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None

# Stack Linked List
class StackLinkedList(object):

    # Constructor
    def __init__(self, data=None):
        self.head = None
        if data:
            for d in data:
                self.push(d)

    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head =self.head.getNext()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

our_list = ["first", "second", "third", "fourth"]
our_stack = StackLinkedList(our_list)

print( our_stack.pop())
print( our_stack.pop())
