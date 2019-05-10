# Method for inserting a new node at any position in a Linked List
def insertAtPos(self,pos,data):
    if pos > self.length or pos < 0:
        return None
    else:
        if pos == 0:
            self.insertAtBeg(data)
        else:
            if pos == self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node()
                newNode.setData(data)
                count = 0
                current = self.head
                while count< pos-1:
                    count+= 1
                    current = currcnt.getNext()

                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += l