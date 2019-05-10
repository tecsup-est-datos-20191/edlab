'''
Created on Mar 10, 2019

@author: jgomezm
'''

# Node of a Single Linked List
class Node(object):

    # Constructor
    def __init__(self, data=None):
        self.data = data

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the next
    def setNext(self, next):
        self.next = next

    # Method for getting the next
    def getNext(self):
        return self.next

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None

class QueueLinkedListsCircular(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.rear
        self.rear = Node(data)

        if self.lastNode:
            self.lastNode.setNext(self.rear)

        if self.front is None:
            self.front = self.rear

        self.size +=1

    def deQueue(self):
        if self.front is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        result = self.front.getData()
        self.front = self.front.next
        self.size -=1
        return result;

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.front.getData()

    def size(self):
        return self.size

# Execution
que = QueueLinkedListsCircular()
que.enQueue("first")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("second")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("third")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("fourth")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("fifth")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("sixth")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("seventh")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
que.enQueue("eighth")
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
print("Dequeuing:" + que.deQueue())
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
print("Dequeuing:" + que.deQueue())
print("Front:" + que.queueFront())
print("Rear:" + que.queueRear())

'''
print("Front:" + que.queueFront())
print("Rear:"+que.queueRear())
print("Dequeuing:" + que.deQueue())
print("Front:" + que.queueFront())
print("Rear:" + que.queueRear())
'''










