class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new = Node(value)

        new.next, new.prev = self.tail, self.tail.prev
        
        self.tail.prev.next, self.tail.prev = new, new

    def appendleft(self, value: int) -> None:
        new = Node(value)

        new.prev, new.next = self.head, self.head.next
        self.head.next.prev, self.head.next = new, new 

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.tail.prev.val

        self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev 

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        value = self.head.next.val

        self.head.next.next.prev, self.head.next  = self.head, self.head.next.next

        return value
