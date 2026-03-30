class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        #Dummy node
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:        
            if i == index:
                return curr.data 
            curr = curr.next
            i += 1
        return -1 #Index out of bounds


    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head

        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []

        while curr:
            values.append(curr.data)
            curr = curr.next
        return values