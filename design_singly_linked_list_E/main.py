class LinkedList:

    class ListNode:
        def __init__(self, value):
            self.value = value
            self.nextNode = None

        def getVal(self):
            return self.value

        def getNext(self):
            return self.nextNode

        def setNext(self, node):
            self.nextNode = node

    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= 0 or index >= self.size or index < 0: return -1

        curNode = self.head
        while index:
            curNode = curNode.getNext()
            index -= 1
        return curNode.getVal()

    def insertHead(self, val: int) -> None:
        newNode = self.ListNode(val)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = self.ListNode(val)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size <= 0 or index >= self.size or index < 0: return False

        prevNode = None
        curNode = self.head
        isTail = index == self.size - 1
        while index:
            prevNode = curNode
            curNode = curNode.getNext()
            index -= 1

        if prevNode:
            prevNode.setNext(curNode.getNext())
            curNode.setNext(None)
            curNode = prevNode
        else:
            self.head = curNode.getNext()
            curNode.setNext(None)
            curNode = self.head
        
        if isTail:
            self.tail = curNode

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        if self.size == 0: return []

        values = []
        curNode = self.head
        while curNode:
            values.append(curNode.getVal())
            curNode = curNode.getNext()

        return values

